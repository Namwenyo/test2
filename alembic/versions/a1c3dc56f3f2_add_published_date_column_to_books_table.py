"""Add published_date column to books table

Revision ID: a1c3dc56f3f2
Revises: 67af98efb269
Create Date: 2025-09-26 14:42:29.385865

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1c3dc56f3f2'
down_revision: Union[str, Sequence[str], None] = '67af98efb269'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
