"""update schema

Revision ID: 9c0b5f9782dd
Revises: 58801a349879
Create Date: 2026-01-11 19:51:27.703737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c0b5f9782dd'
down_revision: Union[str, Sequence[str], None] = '58801a349879'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
