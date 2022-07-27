"""add fk to posts table

Revision ID: 17b4a4653bfd
Revises: 1880d054650d
Create Date: 2022-07-27 18:58:01.446559

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "17b4a4653bfd"
down_revision = "1880d054650d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
