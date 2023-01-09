from logging import Logger, LoggerAdapter
from typing import Any, Dict, Tuple

from pyramid.config import Configurator
from pyramid.request import Request

from ..interfaces import ILoggerAdapterFactory


class WebLoggerAdapter(LoggerAdapter):
    def process(self, msg: str, kwargs: Any) -> Tuple[str, Dict[str, Any]]:
        msg = f"[IP:{self.extra['request'].remote_addr}] {msg}"
        return msg, kwargs


def includeme(config: Configurator) -> None:
    def factory(context: Any, request: Request) -> Any:
        def logger_adapter_factory(logger: Logger) -> LoggerAdapter:
            return WebLoggerAdapter(logger, {"request": request})

        return logger_adapter_factory

    config.register_service_factory(factory, ILoggerAdapterFactory)
