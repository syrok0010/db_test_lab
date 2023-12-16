from time import perf_counter_ns
from library_tests import LibraryTests
from sql_strings import import_csv_sql, create_table_sql, drop_table_sql
import psycopg2_tests, pandas_tests, pandas_inmemory_tests, sqlite_tests, duckdb_tests, sql_alchemy_tests
from psycopg2 import connect
from config_loader import config, tests_count
from io import open
import warnings

warnings.filterwarnings("ignore")


def time(query_func) -> int:
    start = perf_counter_ns()
    query_func()
    end = perf_counter_ns()
    return end - start


def get_tested_libraries():
    all_libraries = LibraryTests.__subclasses__()
    all_enabled_libraries = config['run']
    for key, value in all_enabled_libraries.items():
        if not value:
            continue
        yield next(x for x in all_libraries if x.__name__ == key)


def test_library(tested_library):
    tested_library.setup(config['dataset_path'])
    print('Average time for ' + tested_library.__class__.__name__)
    for query in tested_library.queries:
        total_time: int = 0
        ns_to_s_ratio = 1000000000
        for i in range(0, tests_count):
            total_time += time(query)
        average_time = total_time / tests_count
        print(str(average_time / ns_to_s_ratio))
    tested_library.release()


def init_postgres():
    connection = connect("dbname=postgres user=postgres")
    cur = connection.cursor()
    cur.execute(create_table_sql)
    with open(config['dataset_path']) as csv_file:
        cur.copy_expert(import_csv_sql, csv_file)
    connection.commit()
    cur.close()
    connection.close()


def drop_all():
    connection = connect("dbname=postgres user=postgres")
    cur = connection.cursor()
    cur.execute(drop_table_sql)
    connection.commit()
    cur.close()
    connection.close()


if __name__ == '__main__':
    try:
        init_postgres()
        for libraryClass in get_tested_libraries():
            library = libraryClass()
            test_library(library)
            del library
    finally:
        drop_all()
