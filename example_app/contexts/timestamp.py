import datetime
from typing import Any
from pyramid.config import Configurator
from ..interfaces import ITimestamp


class Timestamp:
    def __init__(self, utcnow: datetime.datetime) -> None:
        self.utcnow = utcnow


def includeme(config: Configurator) -> None:
    def factory(context: Any, request: Any) -> Timestamp:
        return Timestamp(datetime.datetime.utcnow())

    config.register_service_factory(factory, ITimestamp)
