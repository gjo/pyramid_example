import datetime
from logging import Logger, LoggerAdapter
from typing import Any, Optional

from zope.interface import Attribute, Interface


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
    def __call__(logger: Logger) -> LoggerAdapter:
        """
        returns request assigned LoggerAdapter
        """


class IActor(Interface):
    account_id: Optional[int] = Attribute("Account Id")
    account_id_raw: Optional[int] = Attribute("Unauthenticated Account Id")
    api_key_id: Optional[str] = Attribute("API Key Id")
    api_key_id_raw: Optional[str] = Attribute("Unauthenticated API Key Id")
    remote_addr: Optional[str] = Attribute("REMOTE_ADDR from HTTP Headers")
    user_agent: Optional[str] = Attribute("USER_AGENT from HTTP Headers")


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


class IPostQuery(Interface):
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
