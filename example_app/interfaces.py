import datetime
from logging import Logger
from typing import Any

from zope.interface import Attribute, Interface

from .typing import LoggerLike


class IDBEngine(Interface):
    """
    marker for sqlalchemy.engine:Engine
    """


class IDBSession(Interface):
    """
    marker for sqlalchemy.orm.session:Session
    """


class IDBSessionFactory(Interface):
    """
    maker for sqlalchemy.orm.session:sessionmaker
    """


class ILoggerAdapterFactory(Interface):
    def __call__(logger: Logger) -> LoggerLike:
        """
        returns request assigned LoggerAdapter
        """


class IActor(Interface):
    account_id: int | None = Attribute("Account Id")
    account_id_raw: int | None = Attribute("Unauthenticated Account Id")
    api_key_id: str | None = Attribute("API Key Id")
    api_key_id_raw: str | None = Attribute("Unauthenticated API Key Id")
    remote_addr: str | None = Attribute("REMOTE_ADDR from HTTP Headers")
    user_agent: str | None = Attribute("USER_AGENT from HTTP Headers")


class ITimestamp(Interface):
    utcnow: datetime.datetime = Attribute("UTC Timestamp")


class IAccountCommand(Interface):
    def create() -> Any:
        """
        account_create
        """


class IPostCommand(Interface):
    def create(json_body: Any) -> Any:
        """
        post_create
        """

    def delete(post_id: int) -> Any:
        """
        post_delete
        """


class IPostQuery(Interface):
    def find_active_by_id(post_id: int) -> Any:
        """
        post_detail
        """

    def index() -> Any:
        """
        post_index
        """


class IPost(Interface):
    """
    Post Entity
    """

    id: int = Attribute(None, "Post ID")
    text: str = Attribute(None, "Text")
