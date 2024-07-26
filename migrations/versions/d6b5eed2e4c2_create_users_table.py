"""create users table

Revision ID: d6b5eed2e4c2
Revises: 
Create Date: 2024-07-26 13:12:46.895523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6b5eed2e4c2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tb_users',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('nickname', sa.String(24), nullable=False),
        sa.Column('age ', sa.Integer, nullable=True),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('last_login', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime),
                    )


def downgrade() -> None:
    op.drop_table('users')
