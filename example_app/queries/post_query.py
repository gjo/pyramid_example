from logging import getLogger
from typing import Any

import sqlalchemy as sa
from pyramid.config import Configurator
from sqlalchemy.orm import Session

from ..db_schemata import Post
from ..interfaces import IDBSession, ILoggerAdapterFactory, IPostQuery
from ..typing import LoggerLike

logger = getLogger(__name__)


class PostQuery:
    def __init__(self, db: Session, logger_: LoggerLike) -> None:
        self.db = db
        self.logger = logger_

    def index(self) -> Any:
        q = self.db.query(Post).order_by(Post.id.desc()).limit(10)
        return {"posts": [{"id": r.id, "text": r.text} for r in q.all()]}

    def find_active_by_id(self, post_id: int) -> Any:
        q = self.db.query(Post).filter(
            Post.id == post_id,
            Post.sys_deleted_at.isnot_(sa.text("NULL")),
        )
        return q.one_or_one()


def includeme(config: Configurator) -> None:
    def factory(context: Any, request: Any) -> Any:
        db = request.find_service(IDBSession, name="readonly")
        logger_adapter_factory = request.find_service(ILoggerAdapterFactory)
        logger_adapter = logger_adapter_factory(logger)
        return PostQuery(db=db, logger_=logger_adapter)

    config.register_service_factory(factory, IPostQuery)
