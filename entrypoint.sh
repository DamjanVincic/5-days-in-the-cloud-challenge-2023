#!/bin/bash

echo "Applying migrations..."
python3 manage.py migrate

echo "Loading player data..."
python3 manage.py load_player_data

echo "Calculating statistics..."
python3 manage.py calculate_statistics

echo "Starting Django server..."
python3 manage.py runserver 0.0.0.0:8000