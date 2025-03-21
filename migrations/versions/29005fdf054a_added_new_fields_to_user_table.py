"""added new fields to user table

Revision ID: 29005fdf054a
Revises: bf9d0a6c4355
Create Date: 2025-03-19 17:19:10.647087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29005fdf054a'
down_revision = 'bf9d0a6c4355'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_see', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_see')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
