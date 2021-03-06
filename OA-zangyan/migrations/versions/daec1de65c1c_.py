"""empty message

Revision ID: daec1de65c1c
Revises: f58ec39a9172
Create Date: 2019-05-04 20:13:30.582817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daec1de65c1c'
down_revision = 'f58ec39a9172'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchase_management',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('date', sa.String(length=20), nullable=True),
    sa.Column('company', sa.String(length=50), nullable=True),
    sa.Column('link_person', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('should_pay', sa.Integer(), nullable=True),
    sa.Column('react_pay', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchase_management')
    # ### end Alembic commands ###
