from typing import Any

from pyramid.request import Request


class ResourceBase:
    def __init__(self, request: Request) -> None:
        self.request = request

    def delete(self) -> Any:  # pragma: no cover
        raise NotImplementedError

    def get(self) -> Any:  # pragma: no cover
        raise NotImplementedError

    def post(self) -> Any:  # pragma: no cover
        raise NotImplementedError
