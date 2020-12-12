from logging import LoggerAdapter, getLogger
from typing import Any
from pyramid.config import Configurator
from sqlalchemy.orm import Session
from ..db_schemata import Post
from ..interfaces import IDBSession, ILoggerAdapterFactory, IPostCommand


logger = getLogger(__name__)


class PostCommand:
    def __init__(self, db: Session, logger_adapter: LoggerAdapter) -> None:
        self.db = db
        self.logger_adapter = logger_adapter

    def create(self, json_body: Any) -> Any:
        post = Post(text=json_body["text"])
        self.db.add(post)
        self.db.flush()
        self.logger_adapter.info("Post created %r", post.id)
        return {"id": post.id, "text": post.text}


def includeme(config: Configurator) -> None:
    def factory(context: Any, request: Any) -> Any:
        db = request.find_service(IDBSession, name="readwrite")
        logger_adapter_factory = request.find_service(ILoggerAdapterFactory)
        logger_adapter = logger_adapter_factory(logger)
        return PostCommand(db=db, logger_adapter=logger_adapter)

    config.register_service_factory(factory, IPostCommand)
