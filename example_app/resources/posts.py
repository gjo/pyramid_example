from typing import Any

from pyramid.security import Allowed, Denied, PermitsResult

from ..interfaces import IActor, IPostCommand, IPostQuery
from ..openapi import validated_params
from .base import ResourceBase


class PostContainerResource(ResourceBase):
    def __permits__(self, permission: str) -> PermitsResult:
        if permission == "post_read":
            return Allowed
        elif permission == "post_create":
            actor: IActor = self.request.find_service(IActor)
            if actor.account_id:
                return Allowed
        return Denied

    def get(self) -> Any:
        svc: IPostQuery = self.request.find_service(IPostQuery)
        return svc.index()

    def post(self) -> Any:
        svc: IPostCommand = self.request.find_service(IPostCommand)
        params = validated_params(self.request)
        return svc.create(params.body)
