from typing import Any

from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register

from ..interfaces import IDBEngine, IDBSession, IDBSessionFactory


def setup(config: Configurator, name: str) -> None:
    settings = config.registry.settings
    engine = engine_from_config(settings, prefix=f"sqlalchemy.{name}.", logging_name=name)
    config.register_service(engine, IDBEngine, name=name)

    session_factory = sessionmaker(bind=engine)
    config.register_service(session_factory, IDBSessionFactory, name=name)

    def factory(context: Any, request: Any) -> Any:
        session_factory_ = request.find_service(IDBSessionFactory, name=name)
        db = session_factory_()
        db.execute("SET time_zone = '+00:00'")
        register(db, transaction_manager=request.tm)
        return db

    config.register_service_factory(factory, IDBSession, name=name)


def includeme(config: Configurator) -> None:
    setup(config, "readwrite")
