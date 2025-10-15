"""Add published_date column to books table

Revision ID: e632f6c171af
Revises: 51ba830dc0bd
Create Date: 2025-09-26 13:03:53.045691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e632f6c171af'
down_revision: Union[str, Sequence[str], None] = '51ba830dc0bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
