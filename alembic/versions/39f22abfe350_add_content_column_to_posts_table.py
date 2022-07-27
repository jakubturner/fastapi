"""add content column to posts table

Revision ID: 39f22abfe350
Revises: 923dcca27348
Create Date: 2022-07-27 13:16:22.256478

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "39f22abfe350"
down_revision = "923dcca27348"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
