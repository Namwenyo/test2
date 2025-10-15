"""Add published_date column to books table

Revision ID: 1100a533f930
Revises: e05d3d1be155
Create Date: 2025-09-26 16:04:24.178891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1100a533f930'
down_revision: Union[str, Sequence[str], None] = 'e05d3d1be155'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
