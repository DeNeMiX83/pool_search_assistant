"""empty message

Revision ID: 43bb2cf6a671
Revises: 2fc0a9d25f7b
Create Date: 2023-01-22 00:45:26.935578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43bb2cf6a671'
down_revision = '2fc0a9d25f7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('like_pools_pool_id_fkey', 'like_pools', type_='foreignkey')
    op.drop_constraint('like_pools_user_id_fkey', 'like_pools', type_='foreignkey')
    op.create_foreign_key(None, 'like_pools', 'pools', ['pool_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'like_pools', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'like_pools', type_='foreignkey')
    op.drop_constraint(None, 'like_pools', type_='foreignkey')
    op.create_foreign_key('like_pools_user_id_fkey', 'like_pools', 'users', ['user_id'], ['id'])
    op.create_foreign_key('like_pools_pool_id_fkey', 'like_pools', 'pools', ['pool_id'], ['id'])
    # ### end Alembic commands ###
