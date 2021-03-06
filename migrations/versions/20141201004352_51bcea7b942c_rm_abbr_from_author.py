"""Rm abbr from author

Revision ID: 51bcea7b942c
Revises: 11dbdc3ad17f
Create Date: 2014-12-01 00:43:52.070637

"""

# revision identifiers, used by Alembic.
revision = '51bcea7b942c'
down_revision = '11dbdc3ad17f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('author', 'abbr')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author', sa.Column('abbr', mysql.VARCHAR(length=50), nullable=True))
    ### end Alembic commands ###
