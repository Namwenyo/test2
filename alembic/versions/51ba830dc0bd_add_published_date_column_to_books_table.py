"""Add published_date column to books table

Revision ID: 51ba830dc0bd
Revises: your_revision_hash
Create Date: 2025-09-26 12:19:48.149158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51ba830dc0bd'
down_revision: Union[str, Sequence[str], None] = 'your_revision_hash'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
