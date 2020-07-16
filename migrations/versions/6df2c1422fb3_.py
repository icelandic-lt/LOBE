"""empty message

Revision ID: 6df2c1422fb3
Revises: c4d58be3a67f
Create Date: 2020-07-14 16:51:22.690855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6df2c1422fb3'
down_revision = 'c4d58be3a67f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('verifier_progression', sa.Column('last_spin', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('verifier_progression', 'last_spin')
    # ### end Alembic commands ###