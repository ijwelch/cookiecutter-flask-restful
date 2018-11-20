#!/bin/sh

echo "Initalising DB and DATA for {{cookiecutter.app_name}}"

{{cookiecutter.app_name}} init

echo "Starting uwsgi"

uwsgi uwsgi.ini
