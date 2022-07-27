"""add users table

Revision ID: 1880d054650d
Revises: 39f22abfe350
Create Date: 2022-07-27 13:21:54.333938

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "1880d054650d"
down_revision = "39f22abfe350"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
