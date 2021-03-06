from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
log_file = Table('log_file', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user', String(length=120)),
    Column('role', String(length=60)),
    Column('action', String(length=60)),
    Column('description', Text),
    Column('timestamp', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['log_file'].columns['role'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['log_file'].columns['role'].drop()
