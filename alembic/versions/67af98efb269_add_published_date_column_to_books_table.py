"""Add published_date column to books table

Revision ID: 67af98efb269
Revises: 5705f0b1601d
Create Date: 2025-09-26 13:58:38.652625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67af98efb269'
down_revision: Union[str, Sequence[str], None] = '5705f0b1601d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
