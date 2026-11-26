# Динамический сайт на Flask (доп. задание)

Серверная страница: Flask принимает форму, генерирует HTML через шаблон `templates/index.html` и показывает текущее серверное время и счётчик посещений.

## Запуск локально

```powershell
cd dynamic-site
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Откройте http://localhost:5000.

## Публикация

GitHub Pages умеет размещать только статические файлы, поэтому этот проект хранится в репозитории `homework IIT` как исходный код (папка `dynamic-site/`) с инструкцией по запуску. Для работы в интернете приложение нужно разместить на хостинге с поддержкой Python, например Render, PythonAnywhere или Fly.io. В репозиторий добавлен файл `render.yaml` для быстрого развёртывания на Render.

## Структура

- `app.py` — серверная логика и маршрут `/`;
- `templates/index.html` — шаблон страницы;
- `static/style.css` — стили;
- `requirements.txt` — зависимости.
