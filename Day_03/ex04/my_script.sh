#!/bin/bash

# create a virtual environment
python3 -m venv django_venv

# activate the virtual environment
source django_venv/bin/activate

# install Django and psycopg2
pip install -r requirement.txt
