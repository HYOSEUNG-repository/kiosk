"""empty message

Revision ID: 79fe7de4d681
Revises: 3eb75b2e1894
Create Date: 2023-09-21 16:08:23.999217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79fe7de4d681'
down_revision = '3eb75b2e1894'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###