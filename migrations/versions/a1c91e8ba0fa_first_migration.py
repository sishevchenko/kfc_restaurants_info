"""first_migration

Revision ID: a1c91e8ba0fa
Revises: 
Create Date: 2023-07-16 18:07:10.090941

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a1c91e8ba0fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
                    sa.Column('store_id', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=True),
                    sa.Column('street_address', sa.String(), nullable=True),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('latitude', sa.Float(), nullable=True),
                    sa.Column('longitude', sa.Float(), nullable=True),
                    sa.Column('start_time_local', sa.TIME(), nullable=True),
                    sa.Column('end_time_local', sa.TIME(), nullable=True),
                    sa.Column('features', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('store_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant')
    # ### end Alembic commands ###
