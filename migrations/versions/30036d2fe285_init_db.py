"""Init DB

Revision ID: 30036d2fe285
Revises: 
Create Date: 2024-09-01 19:43:18.063786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30036d2fe285'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business_groups',
    sa.Column('_id', sa.BigInteger(), nullable=False),
    sa.Column('biz_status', sa.String(length=45), nullable=False),
    sa.Column('biz_operating', sa.String(length=35), nullable=True),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('biz_operating', 'biz_status', name='uix_status_operating')
    )
    op.create_table('geolocations',
    sa.Column('_id', sa.BigInteger(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('latitude', 'longitude', name='uix_lat_long')
    )
    op.create_table('locations',
    sa.Column('_id', sa.BigInteger(), nullable=False),
    sa.Column('unique_id', sa.String(length=45), nullable=False),
    sa.Column('biz_country_name', sa.String(length=34), nullable=False),
    sa.Column('biz_region_name', sa.String(length=35), nullable=False),
    sa.Column('geolocation_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['geolocation_id'], ['geolocations._id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('unique_id')
    )
    op.create_table('businesses',
    sa.Column('_id', sa.BigInteger(), nullable=False),
    sa.Column('bda_name', sa.String(length=45), nullable=False),
    sa.Column('cohort', sa.String(length=35), nullable=False),
    sa.Column('program', sa.String(length=35), nullable=False),
    sa.Column('group_id', sa.BigInteger(), nullable=True),
    sa.Column('location_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['business_groups._id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations._id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('bda_name')
    )
    op.create_table('assets',
    sa.Column('_id', sa.BigInteger(), nullable=False),
    sa.Column('formhub_uuid', sa.String(length=43), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('endtime', sa.DateTime(), nullable=False),
    sa.Column('cd_survey_date', sa.Date(), nullable=False),
    sa.Column('_status', sa.String(length=25), nullable=False),
    sa.Column('_submission_time', sa.DateTime(), nullable=False),
    sa.Column('__version__', sa.String(length=35), nullable=False),
    sa.Column('meta_instance_id', sa.String(length=55), nullable=False),
    sa.Column('_xform_id_string', sa.String(length=35), nullable=False),
    sa.Column('_uuid', sa.String(length=43), nullable=False),
    sa.Column('_validation_status', sa.JSON(), nullable=True),
    sa.Column('attachments', sa.JSON(), nullable=True),
    sa.Column('notes', sa.JSON(), nullable=True),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('submitted_by', sa.String(length=60), nullable=True),
    sa.Column('business_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['businesses._id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('_uuid')
    )
    op.create_table('clients',
    sa.Column('_id', sa.BigInteger(), nullable=False),
    sa.Column('client_name', sa.String(length=45), nullable=False),
    sa.Column('client_id_manifest', sa.String(length=45), nullable=False),
    sa.Column('location', sa.String(length=45), nullable=False),
    sa.Column('clients_phone', sa.String(length=45), nullable=False),
    sa.Column('clients_phone_smart_feature', sa.String(length=45), nullable=False),
    sa.Column('gender', sa.String(length=45), nullable=False),
    sa.Column('age', sa.String(length=45), nullable=False),
    sa.Column('nationality', sa.String(length=45), nullable=False),
    sa.Column('strata', sa.String(length=45), nullable=False),
    sa.Column('disability', sa.String(length=45), nullable=False),
    sa.Column('education', sa.String(length=45), nullable=False),
    sa.Column('client_status', sa.String(length=45), nullable=False),
    sa.Column('sole_income_earner', sa.String(length=45), nullable=False),
    sa.Column('howrespble_pple', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['businesses._id'], ),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('client_id_manifest')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients')
    op.drop_table('assets')
    op.drop_table('businesses')
    op.drop_table('locations')
    op.drop_table('geolocations')
    op.drop_table('business_groups')
    # ### end Alembic commands ###
