query_sql = [
    'SELECT "VendorID", count(*) FROM taxi GROUP BY 1;',
    'SELECT passenger_count, avg(total_amount) FROM taxi GROUP BY 1;',
    '''
        SELECT
            passenger_count,
            date_part('Year', tpep_pickup_datetime::date),
            count(*) 
        FROM taxi 
        GROUP BY 1, 2;
    ''',
    '''
        SELECT
            passenger_count,
            date_part('Year', tpep_pickup_datetime::date),
            round(trip_distance),
            count(*)
        FROM taxi
        GROUP BY 1, 2, 3
        ORDER BY 2, 4 desc;
    '''

]
