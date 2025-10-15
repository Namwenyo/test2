"""Add published_date column to books table

Revision ID: 5705f0b1601d
Revises: 57dcc0e3d273
Create Date: 2025-09-26 13:06:24.327143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5705f0b1601d'
down_revision: Union[str, Sequence[str], None] = '57dcc0e3d273'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
