import psycopg2

from sql_strings import query_sql
from library_tests import LibraryTests
from config_loader import pg_password


class Psycopg2Tests(LibraryTests):

    def __init__(self):
        super().__init__()
        self.conn = psycopg2.connect(f"dbname=postgres user=postgres password={pg_password}")
        self.cur = self.conn.cursor()

    def setup(self, path: str):
        pass

    def query1(self):
        self.cur.execute(query_sql[0])
        return self.cur.fetchall()

    def query2(self):
        self.cur.execute(query_sql[1])
        return self.cur.fetchall()

    def query3(self):
        self.cur.execute(query_sql[2])
        return self.cur.fetchall()

    def query4(self):
        self.cur.execute(query_sql[3])
        return self.cur.fetchall()

    def release(self):
        self.cur.close()
        self.conn.close()
