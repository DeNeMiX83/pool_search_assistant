"""empty message

Revision ID: 2fc0a9d25f7b
Revises: 
Create Date: 2023-01-22 00:42:13.058363

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2fc0a9d25f7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pools',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('web_site', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('administrative_area', sa.String(), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('has_equipment_rental', sa.Boolean(), nullable=False),
    sa.Column('has_tech_service', sa.Boolean(), nullable=False),
    sa.Column('has_dressing_room', sa.Boolean(), nullable=False),
    sa.Column('has_eatery', sa.Boolean(), nullable=False),
    sa.Column('has_toilets', sa.Boolean(), nullable=False),
    sa.Column('has_wifi', sa.Boolean(), nullable=False),
    sa.Column('has_cash_machine', sa.Boolean(), nullable=False),
    sa.Column('has_first_aid_post', sa.Boolean(), nullable=False),
    sa.Column('has_music', sa.Boolean(), nullable=False),
    sa.Column('is_paid', sa.Boolean(), nullable=False),
    sa.Column('how_suitable_for_disabled', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('like_pools',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pool_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['pool_id'], ['pools.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'pool_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like_pools')
    op.drop_table('users')
    op.drop_table('pools')
    # ### end Alembic commands ###
