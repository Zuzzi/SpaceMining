from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
log_file = Table('log_file', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('user', VARCHAR(length=120)),
    Column('action', VARCHAR(length=60)),
    Column('description', TEXT),
    Column('timestamp', DATETIME),
    Column('role', VARCHAR(length=60)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['log_file'].columns['description'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['log_file'].columns['description'].create()
