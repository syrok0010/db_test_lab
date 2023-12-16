from time import perf_counter_ns
from library_tests import LibraryTests
import psycopg2_tests, pandas_tests, pandas_inmemory_tests, sqlite_tests, duckdb_tests
from json import loads
from io import open
import warnings

warnings.filterwarnings("ignore")

file = open('config.json')
config = json.loads(file.read())
tests_count = config['tests_count']


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
    tested_library.setup('/home/syrok/Downloads/nyc_yellow_tiny.csv')
    for query in tested_library.queries:
        total_time: int = 0
        ns_to_s_ratio = 1000000000
        for i in range(0, tests_count):
            total_time += time(query)
        average_time = total_time / tests_count
        print(
            'Average time for ' +
            str(tested_library.__class__.__name__) + '.' + query.__name__ + ': ' +
            str(average_time / ns_to_s_ratio)
        )


if __name__ == '__main__':
    for libraryClass in get_tested_libraries():
        library = libraryClass()
        test_library(library)
