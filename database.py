from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
import os

DATABASE_URL = f"postgresql+psycopg2://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"

engine = create_engine(DATABASE_URL)                                                # Подключение к базе данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)         # Создание сессии для работы с БД

def create_tables() -> None:                                                        # Функция для создания таблиц
    Base.metadata.create_all(engine)

def get_db():                                                                       # Функция для получения сессии для работы с БД
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()