"""Add published_date column to books table

Revision ID: e05d3d1be155
Revises: a1c3dc56f3f2
Create Date: 2025-09-26 15:45:48.550892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e05d3d1be155'
down_revision: Union[str, Sequence[str], None] = 'a1c3dc56f3f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
