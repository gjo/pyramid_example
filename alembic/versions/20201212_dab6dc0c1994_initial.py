"""initial

Revision ID: dab6dc0c1994
Revises:
Create Date: 2020-12-12 07:06:49.306278+00:00
"""

import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision = "dab6dc0c1994"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accounts",
        sa.Column("id", mysql.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("created_at", mysql.DATETIME(fsp=6), nullable=False),
        sa.Column(
            "deleted_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("NULL"),
            nullable=True,
        ),
        sa.Column(
            "sys_created_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("CURRENT_TIMESTAMP(6)"),
            nullable=False,
        ),
        sa.Column(
            "sys_updated_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"),
            nullable=False,
        ),
        sa.Column(
            "sys_deleted_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("NULL"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_accounts")),
    )
    op.create_index(
        op.f("ix_accounts_created_at"),
        "accounts",
        ["created_at"],
        unique=False,
    )
    op.create_table(
        "posts",
        sa.Column("id", mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("text", mysql.TEXT(), nullable=True),
        sa.Column(
            "sys_created_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("CURRENT_TIMESTAMP(6)"),
            nullable=False,
        ),
        sa.Column(
            "sys_updated_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"),
            nullable=False,
        ),
        sa.Column(
            "sys_deleted_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("NULL"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_posts")),
    )
    op.create_table(
        "api_keys",
        sa.Column("id", mysql.BIGINT(), autoincrement=True, nullable=False),
        sa.Column(
            "secret",
            mysql.VARCHAR(charset="ascii", collation="ascii_bin", length=255),
            nullable=False,
        ),
        sa.Column("account_id", mysql.BIGINT(), nullable=False),
        sa.Column("created_at", mysql.DATETIME(fsp=6), nullable=False),
        sa.Column(
            "deleted_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("NULL"),
            nullable=True,
        ),
        sa.Column(
            "sys_created_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("CURRENT_TIMESTAMP(6)"),
            nullable=False,
        ),
        sa.Column(
            "sys_updated_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"),
            nullable=False,
        ),
        sa.Column(
            "sys_deleted_at",
            mysql.DATETIME(fsp=6),
            server_default=sa.text("NULL"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["account_id"],
            ["accounts.id"],
            name=op.f("fk_api_keys_account_id_accounts"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_api_keys")),
        sa.UniqueConstraint("secret", name=op.f("uq_api_keys_secret")),
    )
    op.create_index(
        op.f("ix_api_keys_created_at"),
        "api_keys",
        ["created_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_api_keys_created_at"), table_name="api_keys")
    op.drop_table("api_keys")
    op.drop_table("posts")
    op.drop_index(op.f("ix_accounts_created_at"), table_name="accounts")
    op.drop_table("accounts")
    # ### end Alembic commands ###
