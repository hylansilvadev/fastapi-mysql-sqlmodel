"""alterando tabela de usuarios

Revision ID: 20cbe9fcfbe9
Revises: 9f902d629710
Create Date: 2024-07-29 20:24:16.298348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20cbe9fcfbe9'
down_revision: Union[str, None] = '9f902d629710'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint('uq_tb_users_nickname', 'tb_users', ['nickname'])


def downgrade() -> None:
    op.drop_constraint('uq_tb_users_nickname', 'tb_users', type_='unique')
