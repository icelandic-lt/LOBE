"""applying mideind changes

Revision ID: baba1508752c
Revises: dca5a3c19137
Create Date: 2024-05-16 12:59:15.271190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baba1508752c'
down_revision = 'dca5a3c19137'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Posting',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('ad_text', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('dev', sa.Boolean(), nullable=True),
    sa.Column('utterances', sa.String(), nullable=True),
    sa.Column('collection', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['collection'], ['Collection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Application',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('voice', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('terms_agreement', sa.Boolean(), nullable=True),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('posting_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['posting_id'], ['Posting.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Application')
    op.drop_table('Posting')
    # ### end Alembic commands ###
