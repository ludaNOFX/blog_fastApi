"""first migration

Revision ID: 642a3a76dbef
Revises: 
Create Date: 2023-10-17 14:07:01.940379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642a3a76dbef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('surname', sa.String(length=80), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('hashed_password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('following',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('original_post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['original_post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_user_id'), 'post', ['user_id'], unique=False)
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('upload_time', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_image_post_id'), 'image', ['post_id'], unique=False)
    op.create_index(op.f('ix_image_user_id'), 'image', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_image_user_id'), table_name='image')
    op.drop_index(op.f('ix_image_post_id'), table_name='image')
    op.drop_table('image')
    op.drop_index(op.f('ix_post_user_id'), table_name='post')
    op.drop_table('post')
    op.drop_table('following')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
