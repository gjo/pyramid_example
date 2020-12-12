from typing import Any
from pyramid.security import Allowed, Denied, PermitsResult
from ..interfaces import IAccountCommand
from .base import ResourceBase


class AccountContainerResource(ResourceBase):
    def __permits__(self, permission: str) -> PermitsResult:
        if permission == "account_create":
            return Allowed
        return Denied

    def post(self) -> Any:
        svc: IAccountCommand = self.request.find_service(IAccountCommand)
        return svc.create()
