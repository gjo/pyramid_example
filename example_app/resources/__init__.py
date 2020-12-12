from pyramid.config import Configurator


def includeme(config: Configurator) -> None:
    from .fallback import FallbackResource

    config.set_root_factory(FallbackResource)
