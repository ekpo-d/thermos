"""manytomany

Revision ID: 50897c4019fd
Revises: 329b876ad97a
Create Date: 2014-10-05 15:36:43.324020

"""

# revision identifiers, used by Alembic.
revision = '50897c4019fd'
down_revision = '329b876ad97a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmark_tag',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('bookmark_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bookmark_id'], ['bookmark.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.drop_index('ix_tag_name', table_name='tag')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_tag_name', 'tag', ['name'], unique=1)
    op.drop_table('bookmark_tag')
    ### end Alembic commands ###
