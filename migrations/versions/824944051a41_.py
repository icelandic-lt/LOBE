"""empty message

Revision ID: 824944051a41
Revises: 0fd98838a675
Create Date: 2019-11-06 13:39:30.862698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824944051a41'
down_revision = '0fd98838a675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Token', sa.Column('source', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Token', 'source')
    # ### end Alembic commands ###