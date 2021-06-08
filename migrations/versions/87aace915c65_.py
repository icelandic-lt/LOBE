"""empty message

Revision ID: 87aace915c65
Revises: 954140d6b159
Create Date: 2021-01-29 16:44:23.656950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87aace915c65'
down_revision = '954140d6b159'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Mos', sa.Column('done_text', sa.String(), nullable=True))
    op.add_column('Mos', sa.Column('use_latin_square', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Mos', 'use_latin_square')
    op.drop_column('Mos', 'done_text')
    # ### end Alembic commands ###