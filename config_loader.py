from json import loads
from io import open

with open('config.json') as file:
    config = loads(file.read())
    tests_count = config['tests_count']
    table_name = config['table_name']
    pg_password = config['pg_password']