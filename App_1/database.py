from statistics import mode
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import crud, models, schemas


SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:ind123@localhost/fastapi_db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}, # only for SQLite
    echo=True, 
    future=True 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(models.metadata.create_all)


# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         autocommit=False, 
#         autoflush=False,
#         bind=engine, 
#         class_=AsyncSession, 
#         expire_on_commit=False
#     )

#     async with async_session() as session:
#         yield session