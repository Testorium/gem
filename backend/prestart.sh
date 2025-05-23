#!/usr/bin/env bash

set -e

echo "Run apply migrations.."

python3 manage.py migrate

if [ $? -ne 0 ]; then
    echo "Failed to apply migrations"
    exit 1
fi

echo "Migrations applied!"

echo "Running application.."

python3 manage.py runserver 0.0.0.0:8000

exec "$@"