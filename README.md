# Тестовое задание: API-сервис для вопросов и ответов

Это простой API‑сервис для вопросов и ответов. Позволяет создавать вопросы, просматривать вопросы (отдельно или весь список), добавлять и читать ответы к заданным вопросам.

## Технологии

- **FastAPI** — веб-фреймворк  
- **SQLAlchemy** — ORM для работы с базой данных  
- **PostgreSQL** — хранилище данных  
- **Alembic** — миграции БД  
- **Docker / Docker Compose** — контейнеризация

## Эндпоинты:

1. Вопросы (Questions):
- GET /questions/ — список всех вопросов
- POST /questions/ — создать новый вопрос
- GET /questions/{id} — получить вопрос и все ответы на него
- DELETE /questions/{id} — удалить вопрос (вместе с ответами)

2. Ответы (Answers):
- POST /questions/{id}/answers/ — добавить ответ к вопросу
- GET /answers/{id} — получить конкретный ответ
- DELETE /answers/{id} — удалить ответ

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/innocentzy/test-api.git
cd test-api 
```

2. Создайте файл .env на основе примера (отредактируйте при необходимости):

```bash
cp .env.example .env
```

3. Запуск проекта через Docker Compose:

```bash
docker-compose up --build
```

4. Доступ к API:
- Swagger: http://localhost:8000/docs

