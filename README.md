# aqa-upgrade-lab

Учебный проект для прокачки Python AQA / Backend QA / API QA.

## Цели проекта

- pytest;
- requests;
- psycopg2;
- PostgreSQL;
- Docker;
- Liquibase;
- GitLab CI/CD;
- Playwright;
- SQL;
- auth checks.

## Запуск тестов

Создать виртуальное окружение:

```powershell
python -m venv venv

Активировать виртуальное окружение:

.\venv\Scripts\Activate.ps1

Установить зависимости:

pip install -r requirements.txt

Запустить все тесты:

pytest -v

Запустить конкретный файл:

pytest .\tests\unit\test_user_validation.py -v