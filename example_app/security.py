from typing import Any
from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.security import Allowed, PermitsResult


class SecurityPolicy:
    def identity(self, request: Request) -> Any:
        pass

    def authenticated_userid(self, request: Request) -> Any:
        pass

    def permits(
        self, request: Request, context: Any, permission: str
    ) -> PermitsResult:
        if hasattr(context, "__permits__"):
            return context.__permits__(permission)
        return Allowed

    def remember(self, request: Request, userid: Any, **kw: Any) -> Any:
        pass

    def forget(self, request: Request, **kw: Any) -> Any:
        pass


def includeme(config: Configurator) -> None:
    config.set_security_policy(SecurityPolicy())
