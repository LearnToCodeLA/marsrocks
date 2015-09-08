"""empty message

Revision ID: 1260fd09c4d4
Revises: 240043bbba94
Create Date: 2015-09-06 01:20:37.469430

"""

# revision identifiers, used by Alembic.
revision = '1260fd09c4d4'
down_revision = '240043bbba94'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visited_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visited_photos')
    ### end Alembic commands ###