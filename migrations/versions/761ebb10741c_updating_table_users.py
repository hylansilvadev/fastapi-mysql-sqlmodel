"""updating table users

Revision ID: 761ebb10741c
Revises: d6b5eed2e4c2
Create Date: 2024-07-29 18:19:00.283922

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "761ebb10741c"
down_revision: Union[str, None] = "d6b5eed2e4c2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # adding columns
    op.add_column("tb_users", sa.Column("first_name", sa.String(24), nullable=True))
    op.add_column("tb_users", sa.Column("last_name", sa.String(24), nullable=True))
    op.add_column("tb_users", sa.Column("image_url", sa.String(255), nullable=True))
    op.add_column("tb_users", sa.Column("birth_date", sa.Date(), nullable=True))

    # dropping columns
    op.drop_column("tb_users", "age")


def downgrade() -> None:
    op.drop_column("tb_users", "first_name")
    op.drop_column("tb_users", "last_name")
    op.drop_column("tb_users", "image_url")
    op.drop_column("tb_users", "birth_date")
