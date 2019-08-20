"""empty message

Revision ID: b69c2c99fe41
Revises: 91ca96ec04e7
Create Date: 2019-08-19 22:43:33.476669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b69c2c99fe41'
down_revision = '91ca96ec04e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Token', sa.Column('collection_id', sa.Integer(), nullable=True))
    op.drop_constraint('Token_collection_fkey', 'Token', type_='foreignkey')
    op.create_foreign_key(None, 'Token', 'Collection', ['collection_id'], ['id'])
    op.drop_column('Token', 'collection')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Token', sa.Column('collection', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Token', type_='foreignkey')
    op.create_foreign_key('Token_collection_fkey', 'Token', 'Collection', ['collection'], ['id'])
    op.drop_column('Token', 'collection_id')
    # ### end Alembic commands ###