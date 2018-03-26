"""crime table

Revision ID: fe0acae6e190
Revises: 
Create Date: 2018-02-22 06:49:17.035968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe0acae6e190'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(precision=10, asdecimal=6), nullable=True),
    sa.Column('longtitude', sa.Float(precision=10, asdecimal=6), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crime')
    # ### end Alembic commands ###
