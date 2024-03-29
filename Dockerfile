FROM python:3.7.4-alpine
# alpine наиболее легковесный образ

MAINTAINER Lutogin App
# Подпись

ENV PYTHONUNBUFFERD 1
# Специальный ключ для работы Python в контейнере, связанный с буферезацией и выводом

COPY ./requirements.txt /requirements.txt
# Копируем с рабочей директории файл с зависимостями в контейнер

RUN apk add --update --no-cache postgresql-client \
        jpeg-dev
        # jpeg-dev для загрузки файлов
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev \
        # Для postgresql
        musl-dev zlib-dev
        # загрузки файлов на сервер

RUN pip install -r /requirements.txt
# Выполним команду установки всех зависимостях описанный в requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
# Указываем рабочую папку
COPY ./app /app
# Копируем содержимое в контейнер

RUN mkdir -p /vol/web/media
# Создание папки для загрузок файлов на сервер
RUN mkdir -p /vol/web/static
# Каталог для статики

RUN adduser -D user
# Создаем пользователя, ключ -D означает, что пользователь создан только для запуска приложения
RUN chown -R user:user /vol/
# Выставим пользователя как владельца директории проекта
RUN chmod -R 755 /vol/web
# Выставим права на директорию WEB

USER user
# Переключение пользователя для виртуальной среды докера.
