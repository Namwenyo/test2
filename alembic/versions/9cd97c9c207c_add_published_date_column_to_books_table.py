from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'your_revision_hash'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Add published_date column
    op.add_column('books', 
        sa.Column('published_date', sa.Date(), nullable=True)
    )

def downgrade():
    # Remove published_date column
    op.drop_column('books', 'published_date')