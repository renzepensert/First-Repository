"""precis

Revision ID: 424fdff8f143
Revises: 18cf85555d68
Create Date: 2020-05-19 16:48:04.780593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '424fdff8f143'
down_revision = '18cf85555d68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rpizza', sa.Column('price11', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rpizza', 'price11')
    # ### end Alembic commands ###