from typing import Any

from pyramid.decorator import reify
from pyramid.exceptions import HTTPNotFound
from pyramid.security import Allowed, Denied, PermitsResult

from ..interfaces import IActor, IPost, IPostCommand, IPostQuery
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


class PostResource(ResourceBase):
    @reify
    def post(self) -> IPost:
        params = validated_params(self.request)
        svc: IPostQuery = self.request.find_service(IPostQuery)
        return svc.find_active_by_id(params.path["postId"])

    def __permits__(self, permission: str) -> PermitsResult:
        if self.post is None:
            raise HTTPNotFound
        if permission == "post_delete":
            actor: IActor = self.request.find_service(IActor)
            if actor.account_id:
                return Allowed
        return Denied

    def delete(self) -> Any:
        svc: IPostCommand = self.request.find_service(IPostCommand)
        return svc.delete()
