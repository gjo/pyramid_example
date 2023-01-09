from pyramid.config import Configurator

from ..interfaces import IDBEngine, IDBSession, IDBSessionFactory
from .db_readwrite import setup


def single_instance(config: Configurator) -> None:
    config.register_service_factory(
        lambda c, r: r.find_service(IDBEngine, name="readwrite"),
        IDBEngine,
        name="readonly",
    )
    config.register_service_factory(
        lambda c, r: r.find_service(IDBSessionFactory, name="readwrite"),
        IDBSessionFactory,
        name="readonly",
    )
    config.register_service_factory(
        lambda c, r: r.find_service(IDBSession, name="readwrite"),
        IDBSession,
        name="readonly",
    )


def includeme(config: Configurator) -> None:  # pragma: no cover
    setup(config, "readonly")
