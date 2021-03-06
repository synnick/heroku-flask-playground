"""create initial tables
Revision ID: e8d0b1f54f4e
Revises:
Create Date: 2017-09-16 20:54:23.416219
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8d0b1f54f4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'access_logs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'when',
            sa.DateTime,
            server_default=sa.func.current_timestamp()
        ),
    )


def downgrade():
    op.drop_table('access_logs')
