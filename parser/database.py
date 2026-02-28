from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite+aiosqlite:///wb_parser.sqlite3"
engine = create_async_engine(DATABASE_URL,
                             echo=False)

async_session = async_sessionmaker(engine, expire_on_commit=False)


