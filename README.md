### Hexlet tests and linter status:
[![Actions Status](https://github.com/chustovalena/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/chustovalena/python-project-52/actions)

### Test - Coverage:
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=chustovalena_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=chustovalena_python-project-52)


# 🔧 Task Manager — управление задачами

Task Manager — это полнофункциональное веб-приложение на Django.
Сервис реализует базовую логику трекера задач и обеспечивает удобное управление рабочими процессами: от создания задач до их фильтрации по статусам, исполнителям и меткам. Сервис поддерживает локализацию и имеет удобный UI на основе Bootstrap 5.

Приложение развёрнуто на Render:

👉 https://python-project-52-xblt.onrender.com

---

## ✅ Основные возможности

### 👥 Пользователи
- Регистрация
- Авторизация / выход
- Просмотр списка пользователей
- Редактирование и удаление (только собственный аккаунт)
- Flash-сообщения об успехах и ошибках

### Задачи

- Создание, обновление, удаление
- Назначение статуса, меток(Many-to-Many) и исполнителя
- Просмотр детальной страницы
- CRUD с проверкой прав (удалять/изменять может только автор)

### Фильтры

- Через django-filter доступны параметры:
- статус
- исполнитель
- метки
- только свои задачи

### Локализация

- 🇬🇧 English
- 🇷🇺 Russian
- Переводы хранятся по приложениям (locale/ru/LC_MESSAGES)

### Интерфейс

- Bootstrap 5 через django-bootstrap5
- Общий шаблон base.html
- Разделение шаблонов по приложениям

### Логирование ошибок

- Интеграция с Rollbar для продакшена
- В dev вывод логов в консоль

### Статика

- Whitenoise
- В продакшене — автоматическая сборка статики

### Далее будет реализовано
- Docker ✅
- redis

---

## ⚙️ Используемые технологии

- Python 3.13
- Django 5
- Django ORM
- Jinja2
- django-filter
- Bootstrap
- Whitenoise
- Gunicorn
- PostgreSQL (Render)
- SQLite (локально)
- uv
- pytest + pytest-django + pytest-cov
- ruff
- i18n

---

## Установка и запуск

## 🚀 Локальный запуск через Docker


1. **Склонируйте репозиторий и перейдите в директорию проекта:**
   ```bash
   git clone https://github.com/chustovalena/python-project-52.git
   cd python-project-52
   ```
2. **Создайте файлы окружения на основе примеров:**
   ```bash
   cp .env.example .env
   ```
3. **Поднимите Docker:**
   ```bash
   make docker
   ```
4. **Применить миграции:**
   ```bash
   docker exec -it task_manager_web uv run manage.py migrate
   ```
5. **Сайт будет доступен по адресу:**
   ➡️ http://127.0.0.1:8000