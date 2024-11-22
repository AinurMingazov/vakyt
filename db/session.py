import os
from typing import Generator

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import url
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())

ASYNC_DATABASE_URL = url.URL.create(
    drivername='postgresql+asyncpg',
    database=os.getenv('POSTGRES_DB', 'postgres'),
    port=int(os.getenv('POSTGRES_PORT', '5454')),
    host=os.getenv('POSTGRES_HOST', 'localhost'),
    username=os.getenv('POSTGRES_USER', 'postgres'),
    password=os.getenv('POSTGRES_PASSWORD', 'postgres'),
)

SYNC_DATABASE_URL = url.URL.create(
    drivername='postgresql+psycopg2',
    database=os.getenv('POSTGRES_DB', ''),
    port=int(os.getenv('POSTGRES_PORT', '5432')),
    host=os.getenv('POSTGRES_HOST', ''),
    username=os.getenv('POSTGRES_USER', ''),
    password=os.getenv('POSTGRES_PASSWORD', ''),
)


engine = create_async_engine(
    ASYNC_DATABASE_URL, future=True, echo=True, execution_options={'isolation_level': 'AUTOCOMMIT'}
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

sync_engine = create_engine(SYNC_DATABASE_URL)
sync_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=sync_engine))


async def get_db_session() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        async with session.begin():
            yield session
    except Exception as e:
        print(f'try get db session {e}')
