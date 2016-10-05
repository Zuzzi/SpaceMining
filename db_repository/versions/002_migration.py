from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
job_position = Table('job_position', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('job', String(length=120)),
    Column('description', String(length=120)),
    Column('requirements', String(length=120)),
    Column('picture', String(length=60)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['job_position'].columns['picture'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['job_position'].columns['picture'].drop()
