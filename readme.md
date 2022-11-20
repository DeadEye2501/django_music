## Тестовый проект музыкальной библиотеки

### Используемый стек:
* `django`
* `django rest framework`
* `swagger`
* `docker`

### Для развёртывания приложения необходимо:

* установить Docker: https://www.docker.com/
* клонировать репозиторий
* в корневой папке выполнить команду `docker-compose up -d --build`
* сервер должен быть доступен на `localhost:8000`
* для администрирования нужно создать суперпользователя `python manage.py createsuperuser`

### Доступные API

* swagger доступен по адресу http://localhost:8000/api/schema/swagger-ui/ там вы найдёте все используемые в проекте эндпоинты