"""initial tables

Revision ID: 692f4b9b8e85
Revises: 
Create Date: 2022-07-30 23:40:46.719589

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '692f4b9b8e85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exchanges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('source_amount', sa.Float(), nullable=False),
    sa.Column('source_currency', sa.String(), nullable=False),
    sa.Column('target_currencies', postgresql.ARRAY(sa.String()), nullable=False),
    sa.Column('target_amounts', postgresql.ARRAY(sa.Float()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exchanges')
    # ### end Alembic commands ###
