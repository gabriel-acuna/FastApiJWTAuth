"""cambio de logintud de la columna nombre en la tabla capacitaciones

Revision ID: 26d5745ee8ec
Revises: abec984c3c0f
Create Date: 2021-11-30 09:07:35.818450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d5745ee8ec'
down_revision = 'abec984c3c0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("capacitaciones", "nombre", existing_type=sa.String(30),  type_= sa.String(120), existing_nullable=False)
    

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("capacitaciones", "nombre", existing_type=sa.String(120), type_= sa.String(30), existing_nullable=False)
    # ### end Alembic commands ###
