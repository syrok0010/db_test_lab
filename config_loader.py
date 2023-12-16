file = open('config.json')
config = loads(file.read())
tests_count = config['tests_count']
table_name = config['table_name']