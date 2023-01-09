from pyramid.config import Configurator

from .resources.accounts import AccountContainerResource
from .resources.posts import PostContainerResource


def includeme(config: Configurator) -> None:
    config.add_route("root", pattern="/")
    config.add_route("posts", pattern="/posts/", factory=PostContainerResource)
    config.add_route("accounts", pattern="/accounts/", factory=AccountContainerResource)
