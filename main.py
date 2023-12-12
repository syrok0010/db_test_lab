from time import perf_counter_ns
from library_tests import LibraryTests
import psycopg2_tests, pandas_tests, pandas_inmemory_tests

tests_count = 5


def time(query_func) -> int:
    start = perf_counter_ns()
    query_func()
    end = perf_counter_ns()
    return end - start


def get_tested_libraries():
    return LibraryTests.__subclasses__()


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
            str(libraryClass.__name__) + '.' + query.__name__ + ': ' +
            str(average_time / ns_to_s_ratio)
        )


if __name__ == '__main__':
    for libraryClass in get_tested_libraries():
        library = libraryClass()
        test_library(library)
    pass
