from typing import Any

from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.view import view_config

OAS_DELETE = dict(openapi=True, renderer="json", request_method="DELETE")
OAS_GET = dict(openapi=True, renderer="json", request_method="GET")
OAS_POST_JSON = dict(
    openapi=True,
    renderer="json",
    request_method="POST",
    header="Content-Type:application/json",
)


@view_config(route_name="root", **OAS_GET)
def blank_view(request: Request) -> Any:
    return {}


@view_config(route_name="post", permission="post_delete", **OAS_DELETE)
def resource_delete_view(request: Request) -> Any:
    return request.context.delete()


@view_config(route_name="posts", permission="post_read", **OAS_GET)
def resource_get_view(request: Request) -> Any:
    return request.context.get()


@view_config(route_name="accounts", permission="account_create", **OAS_POST_JSON)
@view_config(route_name="posts", permission="post_create", **OAS_POST_JSON)
def resource_post_view(context: Any, request: Request) -> Any:
    return request.context.post()


def includeme(config: Configurator) -> None:
    config.scan(".")
