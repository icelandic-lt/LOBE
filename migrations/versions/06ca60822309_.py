"""empty message

Revision ID: 06ca60822309
Revises: 9099ee53900a
Create Date: 2020-08-06 17:25:45.133618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ca60822309'
down_revision = '9099ee53900a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SynthToken',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('original_fname', sa.String(), nullable=True),
    sa.Column('mos_id', sa.Integer(), nullable=True),
    sa.Column('synth_id', sa.Integer(), nullable=True),
    sa.Column('fname', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('marked_as_bad', sa.Boolean(), nullable=True),
    sa.Column('num_recordings', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mos_id'], ['Mos.id'], ),
    sa.ForeignKeyConstraint(['synth_id'], ['Synth.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Synth', sa.Column('synthToken_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Synth', 'SynthToken', ['synthToken_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Synth', type_='foreignkey')
    op.drop_column('Synth', 'synthToken_id')
    op.drop_table('SynthToken')
    # ### end Alembic commands ###