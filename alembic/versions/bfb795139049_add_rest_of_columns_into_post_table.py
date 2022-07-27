"""add rest of columns into post table

Revision ID: bfb795139049
Revises: 17b4a4653bfd
Create Date: 2022-07-27 19:04:10.748025

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "bfb795139049"
down_revision = "17b4a4653bfd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created")
    pass
