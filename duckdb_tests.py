from library_tests import LibraryTests
from sql_strings import query_sql
import duckdb


class DuckDBTests(LibraryTests):
    def setup(self, path: str):
        duckdb.sql(f'''CREATE TABLE taxi AS FROM '{path}';''')

    def query1(self):
        return duckdb.sql(query_sql[0])

    def query2(self):
        return duckdb.sql(query_sql[1])

    def query3(self):
        return duckdb.sql(query_sql[2])

    def query4(self):
        return duckdb.sql(query_sql[3])
