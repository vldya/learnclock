"""google_auth

Revision ID: 81587e545077
Revises: 50a215130869
Create Date: 2025-01-12 17:44:16.215379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81587e545077'
down_revision: Union[str, None] = '50a215130869'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('UserProfile', sa.Column('google_access_token', sa.String(), nullable=True))
    op.add_column('UserProfile', sa.Column('email', sa.String(), nullable=True))
    op.add_column('UserProfile', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('UserProfile', 'name')
    op.drop_column('UserProfile', 'email')
    op.drop_column('UserProfile', 'google_access_token')
    # ### end Alembic commands ###
