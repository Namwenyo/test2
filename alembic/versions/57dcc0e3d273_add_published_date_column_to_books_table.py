"""Add published_date column to books table

Revision ID: 57dcc0e3d273
Revises: e632f6c171af
Create Date: 2025-09-26 13:05:58.842038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57dcc0e3d273'
down_revision: Union[str, Sequence[str], None] = 'e632f6c171af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
