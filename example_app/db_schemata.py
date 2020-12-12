from sqlalchemy import Column, ForeignKey, MetaData, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

NAMING_CONVENTION = {
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "ix": "ix_%(column_0_label)s",
    "pk": "pk_%(table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
}
metadata = MetaData(naming_convention=NAMING_CONVENTION)


class DBSchema:
    sys_created_at = Column(
        DATETIME(fsp=6),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP(6)"),
    )
    sys_updated_at = Column(
        DATETIME(fsp=6),
        nullable=False,
        server_default=text(
            "CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"
        ),
    )
    sys_deleted_at = Column(
        DATETIME(fsp=6), nullable=True, server_default=text("NULL")
    )

    # hack for column creation order
    sys_created_at._creation_order = 2000  # type: ignore
    sys_updated_at._creation_order = 2001  # type: ignore
    sys_deleted_at._creation_order = 2002  # type: ignore


Base = declarative_base(metadata=metadata, cls=DBSchema)


class Account(Base):
    __tablename__ = "accounts"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    created_at = Column(DATETIME(fsp=6), nullable=False, index=True)
    deleted_at = Column(
        DATETIME(fsp=6), nullable=True, server_default=text("NULL")
    )


class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    secret = Column(
        VARCHAR(255, charset="ascii", collation="ascii_bin"),
        nullable=False,
        unique=True,
    )
    account_id = Column(
        BIGINT,  # FIXME: 本来書く必要はないけどsqlalchemy-stubが対応してない
        ForeignKey(Account.id),
        nullable=False,
    )
    created_at = Column(DATETIME(fsp=6), nullable=False, index=True)
    deleted_at = Column(
        DATETIME(fsp=6), nullable=True, server_default=text("NULL")
    )

    account = relationship(Account, innerjoin=True, uselist=False)


class Post(Base):
    """
    Post Entity
    """

    __tablename__ = "posts"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    text = Column(TEXT)
