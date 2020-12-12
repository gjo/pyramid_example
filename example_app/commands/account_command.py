import uuid
from logging import LoggerAdapter, getLogger
from typing import Any
from pyramid.config import Configurator
from sqlalchemy.orm import Session
from ..db_schemata import Account, ApiKey
from ..interfaces import (
    IAccountCommand,
    IDBSession,
    ILoggerAdapterFactory,
    ITimestamp,
)


logger = getLogger(__name__)


class AccountCommand:
    def __init__(
        self, db: Session, logger_adapter: LoggerAdapter, timestamp: ITimestamp
    ) -> None:
        self.db = db
        self.logger_adapter = logger_adapter
        self.timestamp = timestamp

    def create(self) -> Any:
        account = Account(created_at=self.timestamp.utcnow)
        self.db.add(account)
        self.db.flush()
        api_key = ApiKey(
            secret=str(uuid.uuid4()),
            account_id=account.id,
            created_at=self.timestamp.utcnow,
        )
        self.db.add(api_key)
        self.db.flush()
        self.logger_adapter.info(
            "Account Created: %r, %r", account.id, api_key.id
        )
        return {"token": api_key.secret}


def includeme(config: Configurator) -> None:
    def factory(context: Any, request: Any) -> Any:
        db = request.find_service(IDBSession, name="readwrite")
        logger_adapter_factory = request.find_service(ILoggerAdapterFactory)
        logger_adapter = logger_adapter_factory(logger)
        timestamp = request.find_service(ITimestamp)
        return AccountCommand(
            db=db, logger_adapter=logger_adapter, timestamp=timestamp
        )

    config.register_service_factory(factory, IAccountCommand)
