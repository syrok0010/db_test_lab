from setuptools import setup, find_packages

setup(
    name='benchmark-libs-lab',
    version='0.0.1',
    description='Lab on benchmarking of different data access libraries',
    author='Vadim Syrov',
    author_email='vasyrov@edu.hse.ru',
    packages=find_packages(),
    install_requires=[
        'psycopg2',
        'sqlalchemy',
        'pandas',
        'duckdb'
    ],
)
