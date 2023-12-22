"""created VisitedLink

Revision ID: 4525da27bcf4
Revises: 
Create Date: 2023-12-22 22:24:30.682199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4525da27bcf4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "visited_link",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("link", sa.String(), nullable=False),
        sa.Column("domain", sa.String(), nullable=False),
        sa.Column("visited_at", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("visited_link")
    # ### end Alembic commands ###