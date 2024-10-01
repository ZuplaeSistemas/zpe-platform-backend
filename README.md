# Zpe-platform-backend


alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000