from abc import ABC

from library_tests import LibraryTests
import sqlite3
from pandas import read_csv
from sql_strings import query_sql_sqlite as query_sql
from config_loader import table_name


class SQLiteTests(LibraryTests):
    def __init__(self):
        super().__init__()
        self.cur = None
        self.conn = None

    def setup(self, path: str):
        self.conn = sqlite3.connect(':memory:')
        read_csv(path).to_sql(table_name, self.conn, if_exists='replace', index=False)
        self.cur = self.conn.cursor()
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
        if self.conn is not None:
            self.cur.close()
            self.conn.close()
