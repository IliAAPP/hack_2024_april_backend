# ${message}
from alembic import op
import sqlalchemy as sa
from datetime import datetime

revision = '7342a59afc14'
down_revision = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('permissions', sa.JSON())
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('registered_at', sa.TIMESTAMP(), default=datetime.utcnow),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'))
    )



def downgrade():
    op.drop_table('users')
    op.drop_table('roles')

