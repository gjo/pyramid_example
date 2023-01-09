import datetime

from pyramid.config import Configurator
from pyramid.interfaces import IRequest
from pyramid.renderers import JSON


def json_date_adapter(d: datetime.date, request: IRequest) -> str:
    return d.strftime("%Y-%m-%d")


def json_datetime_adapter(dt: datetime.datetime, request: IRequest) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def includeme(config: Configurator) -> None:
    config.add_renderer(
        "json",
        JSON(
            ensure_ascii=False,
            separators=(",", ":"),
            adapters=[
                (datetime.date, json_date_adapter),
                (datetime.datetime, json_datetime_adapter),
            ],
        ),
    )
