"""adicionando campo email

Revision ID: 9f902d629710
Revises: 761ebb10741c
Create Date: 2024-07-29 19:24:59.689088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f902d629710'
down_revision: Union[str, None] = '761ebb10741c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("tb_users", sa.Column("email", sa.String(45), nullable=False))


def downgrade() -> None:
    op.drop_column("tb_users", "email")
    
