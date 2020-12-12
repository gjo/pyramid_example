from logging import getLogger
from typing import Any
from pyramid.config import Configurator

__version__ = "0.1.dev0"

WSGIApplication = Any

components = [
    "pyramid_services",
    "pyramid_tm",
    "pyramid_openapi3",
    ".commands.account_command",
    ".commands.post_command",
    ".connectors.db_readonly",
    ".connectors.db_readwrite",
    ".contexts.actor",
    ".contexts.logger_adapter",
    ".contexts.timestamp",
    ".openapi",
    ".queries.post_query",
    ".renderers",
    ".resources",
    ".routes",
    ".security",
    ".views",
]
default_settings = {
    "pyramid_openapi3.enable_request_validation": "true",
    "pyramid_openapi3.enable_response_validation": "true",
    # "sqlalchemy.readonly.url": "REQUIRED",
    "sqlalchemy.readonly.pool_recycle": "3600",
    # "sqlalchemy.readwrite.url": "REQUIRED",
    "sqlalchemy.readwrite.pool_recycle": "3600",
    "tm.manager_hook": "pyramid_tm.explicit_manager",
}
logger = getLogger(__name__)


def includeme(config: Configurator) -> None:
    from . import db_schemata  # noqa: F401;  load schema

    settings = config.registry.settings
    for c in components:
        ckey = f"example_app.components.{c}"
        if ckey in settings:
            config.include(settings[ckey])
        else:
            config.include(c)


def app_factory(global_config: Any, **settings: Any) -> WSGIApplication:
    app_settings = default_settings.copy()
    app_settings.update(settings)
    config = Configurator(settings=app_settings)
    config.include(".")
    app: WSGIApplication = config.make_wsgi_app()
    logger.info("Application created")
    return app


def pshell_setup(env: Any) -> Any:  # pragma: no cover
    from contextlib import suppress
    from transaction.interfaces import NoTransaction
    from .interfaces import IDBSession

    request = env["request"]
    env["tm"] = request.tm

    request.tm.begin()
    try:
        env["db"] = request.find_service(IDBSession, name="readonly")
        env["db_write"] = request.find_service(IDBSession, name="readwrite")
        yield
    finally:
        with suppress(NoTransaction):
            request.tm.abort()
