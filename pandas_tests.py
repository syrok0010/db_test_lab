import pandas as pd
from sqlalchemy import create_engine

from sql_strings import query_sql
from library_tests import LibraryTests


class PandasTests(LibraryTests):

    def setup(self, path: str):
        pass

    def query1(self):
        return pd.read_sql_query(query_sql[0], self.conn)

    def query2(self):
        return pd.read_sql_query(query_sql[1], self.conn)

    def query3(self):
        return pd.read_sql_query(query_sql[2], self.conn)

    def query4(self):
        return pd.read_sql_query(query_sql[3], self.conn)

    def __init__(self):
        super().__init__()
        self.alchemy_engine = create_engine('postgresql+psycopg2://postgres:@127.0.0.1:5432/postgres')
        self.conn = self.alchemy_engine.connect()

    def release(self):
        self.alchemy_engine.dispose()
