from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import NullPool

from app.config import settings


def make_dsn(test: bool = False):
    host = settings.db_host
    user = settings.db_user
    password = settings.db_password
    port = settings.db_port
    if not test:
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{settings.db_name}"
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{settings.test_db_name}"


engine = create_async_engine(make_dsn())
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


test_engine = create_async_engine(make_dsn(test=True), poolclass=NullPool)
test_sessionmaker = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

async def get_test_session() -> AsyncSession:
    async with test_sessionmaker() as session:
        yield session
