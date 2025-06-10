# Установка и запуск докере

1. Переименовать **.env-sample** в **.env**
2. Установить uv
3. Выполнить: `./export_requirements.sh`
4. Выполнить: `sudo docker-compose up --build`

если нужно пересобрать
```
sudo docker-compose down -v 
sudo docker-compose build --no-cache 
sudo docker-compose up
```

---
# ruff

- Запуск в качестве линтера:
`ruff check .`
- Запуск авто форматирования:
`ruff format .`
#### Как сделать [интеграцию ruff в PyCharm](./readme_ruff_integration.md) 


---
# Alembic

- Создание миграции: ```alembic revision --autogenerate -m "comment" --rev-id XXXX(порядковый id)``` 
- Изменить название миграции добавив порядковый номер, включить миграцию в гит
- Применение миграции: ```alembic upgrade heads```

---

# uv
Установка `curl -LsSf https://astral.sh/uv/install.sh | sh`

В папке проекта из терминала и ввести `uv init` `uv sync`

Активация виртуального окружения  `source .venv/bin/activate`