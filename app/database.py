from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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

create_tables()