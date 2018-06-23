"""Add news d

Revision ID: d5d507414bae
Revises: 79ac1941d54b
Create Date: 2018-06-23 11:01:29.859865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d507414bae'
down_revision = '79ac1941d54b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'content')
    # ### end Alembic commands ###
