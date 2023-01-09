from pyramid.config import Configurator

from .resources.accounts import AccountContainerResource
from .resources.posts import PostContainerResource, PostResource


def includeme(config: Configurator) -> None:
    config.add_route("root", pattern="/")
    config.add_route("posts", pattern="/posts/", factory=PostContainerResource)
    config.add_route("post", pattern="/posts/{postId}/", factory=PostResource)
    config.add_route("accounts", pattern="/accounts/", factory=AccountContainerResource)
