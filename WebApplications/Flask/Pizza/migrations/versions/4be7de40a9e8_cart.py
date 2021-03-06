"""cart

Revision ID: 4be7de40a9e8
Revises: 09a0e3b4cb7b
Create Date: 2020-05-15 13:07:05.577633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4be7de40a9e8'
down_revision = '09a0e3b4cb7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('order', sa.String(), nullable=True),
    sa.Column('total', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    # ### end Alembic commands ###
