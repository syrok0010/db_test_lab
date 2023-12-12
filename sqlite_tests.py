from abc import ABC

from library_tests import LibraryTests
import sqlite3
from pandas import read_csv
from sql_strings import query_sql


class SQLiteTests(LibraryTests):
    def __init__(self):
        super().__init__()
        self.cur = None
        self.conn = None

    def setup(self, path: str):
        self.conn = sqlite3.connect(":memory:")
        read_csv(path).to_sql('taxi', self.conn, if_exists='replace', index=False)
        self.cur = self.conn.cursor()
        pass

    def query1(self):
        self.cur.execute(query_sql[0])
        return self.cur.fetchall()

    def query2(self):
        self.cur.execute(query_sql[1])
        return self.cur.fetchall()

    def query3(self):
        self.cur.execute(
            '''
                SELECT
                    passenger_count,
                    strftime('%Y', tpep_pickup_datetime) AS "Year",
                    count(*) 
                FROM taxi 
                GROUP BY 1, 2;
            '''
        )
        return self.cur.fetchall()

    def query4(self):
        self.cur.execute(
            '''
                SELECT
                    passenger_count,
                    strftime('%Y', tpep_pickup_datetime) AS "Year",
                    round(trip_distance),
                    count(*)
                FROM taxi
                GROUP BY 1, 2, 3
                ORDER BY 2, 4 desc;
            '''
        )
        return self.cur.fetchall()

    def __del__(self):
        self.cur.close()
        self.conn.close()