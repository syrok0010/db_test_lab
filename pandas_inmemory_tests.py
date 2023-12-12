import pandas as pd

from library_tests import LibraryTests
from pandas import DataFrame, read_csv


class PandasInMemoryTests(LibraryTests):

    def __init__(self):
        super().__init__()
        self.pd = None
        self.taxi = None

    def setup(self, path: str):
        self.pd = read_csv(path)
        self.taxi = DataFrame(self.pd)

    def query1(self):
        selected_df = self.taxi[['VendorID']]
        grouped_df = selected_df.groupby('VendorID')
        return grouped_df.size().reset_index(name='counts')

    def query2(self):
        selected_df = self.taxi[['passenger_count', 'total_amount']]
        grouped_df = selected_df.groupby('passenger_count')
        return grouped_df.mean().reset_index()

    def query3(self):
        selected_df = self.taxi[['passenger_count', 'tpep_pickup_datetime']]
        selected_df['year'] = pd.to_datetime(
            selected_df.pop('tpep_pickup_datetime'),
            format='%Y-%m-%d %H:%M:%S').dt.year
        grouped_df = selected_df.groupby(['passenger_count', 'year'])
        return grouped_df.size().reset_index(name='counts')

    def query4(self):
        selected_df = self.taxi[[
            'passenger_count',
            'tpep_pickup_datetime',
            'trip_distance']]
        selected_df['trip_distance'] = selected_df['trip_distance'].round().astype(int)
        selected_df['year'] = pd.to_datetime(
            selected_df.pop('tpep_pickup_datetime'),
            format='%Y-%m-%d %H:%M:%S').dt.year
        grouped_df = selected_df.groupby([
            'passenger_count',
            'year',
            'trip_distance'])
        return grouped_df.size().reset_index(name='counts').sort_values(['year', 'counts'], ascending=[True, False])

    def __del__(self):
        del self.taxi
        del self.pd
