from dataclasses import dataclass
from typing import Any, Optional

from pyramid.config import Configurator
from pyramid.request import Request
from sqlalchemy import text

from ..db_schemata import Account, ApiKey
from ..interfaces import IActor, IDBSession


@dataclass
class Actor:
    account_id: Optional[int]
    account_id_raw: Optional[int]
    api_key_id: Optional[str]
    api_key_id_raw: Optional[str]
    remote_addr: Optional[str]
    user_agent: Optional[str]


def factory(context: Any, request: Request) -> Actor:
    account_id = None
    account_id_raw = None
    api_key_id = None
    api_key_id_raw = None
    remote_addr = request.remote_addr
    user_agent = request.user_agent
    api_key_secret = request.headers.get("X-Api-Key")
    if api_key_secret:
        db = request.find_service(IDBSession, name="readonly")
        q = (
            db.query(
                # SQLAlchemyのキャッシュを回避するため、必ず属性単位で検索する。
                ApiKey.id.label("api_key_id"),
                ApiKey.deleted_at.label("api_key_deleted_at"),
                Account.id.label("account_id"),
                Account.deleted_at.label("account_deleted_at"),
            )
            .select_from(ApiKey)
            .join(Account)
            .filter(
                ApiKey.secret == api_key_secret,
                ApiKey.sys_deleted_at.is_(text("NULL")),
                Account.sys_deleted_at.is_(text("NULL")),
            )
        )
        row = q.one_or_none()
        if row:
            account_id_raw = row.account_id
            api_key_id_raw = row.api_key_id
            if row.api_key_deleted_at is None:
                api_key_id = api_key_id_raw
                if row.account_deleted_at is None:
                    account_id = account_id_raw
    return Actor(
        account_id=account_id,
        account_id_raw=account_id_raw,
        api_key_id=api_key_id,
        api_key_id_raw=api_key_id_raw,
        remote_addr=remote_addr,
        user_agent=user_agent,
    )


def includeme(config: Configurator) -> None:
    config.register_service_factory(factory, IActor)
