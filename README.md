
---
# ruff

- Запуск в качестве линтера:
`ruff check .`
- Запуск авто форматирования:
`ruff format .`
#### Как сделать [интеграцию ruff в PyCharm](./readme_ruff_integration.md) 


---
# poetry

Зависимости устанавливаются\добавляются с помощью утилиты `poetry` . [Установка](https://python-poetry.org/docs/)

В папке проекта из терминала и ввести `poetry build` `poetry install`. 

Poetry создаст виртуальное окружение в папке `.venv` проекта.

Активация виртуального окружения  `poetry shell` 

---
# Alembic

- Создание миграции: ```alembic revision --autogenerate -m "comment" --rev-id XXXX(порядковый id)``` 
- Изменить название миграции добавив порядковый номер, включить миграцию в гит
- Применение миграции: ```alembic upgrade heads```

---

