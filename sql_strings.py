from config_loader import table_name

query_sql = [
    f'SELECT "VendorID", count(*) FROM {table_name} GROUP BY 1;',
    f'SELECT passenger_count, avg(total_amount) FROM {table_namee} GROUP BY 1;',
    f'''
        SELECT
            passenger_count,
            date_part('Year', tpep_pickup_datetime::date),
            count(*) 
        FROM {table_name}
        GROUP BY 1, 2;
    ''',
    f'''
        SELECT
            passenger_count,
            date_part('Year', tpep_pickup_datetime::date),
            round(trip_distance),
            count(*)
        FROM {table_name}
        GROUP BY 1, 2, 3
        ORDER BY 2, 4 desc;
    '''
]

query_sql_sqlite = [
    f'SELECT "VendorID", count(*) FROM {table_name} GROUP BY 1;',
    f'SELECT passenger_count, avg(total_amount) FROM {table_namee} GROUP BY 1;',
    f'''
        SELECT
            passenger_count,
            strftime('%Y', tpep_pickup_datetime) AS "Year",
            count(*) 
        FROM {table_name} 
        GROUP BY 1, 2;
    ''',
    f'''
        SELECT
            passenger_count,
            strftime('%Y', tpep_pickup_datetime) AS "Year",
            round(trip_distance),
            count(*)
        FROM {table_name}
        GROUP BY 1, 2, 3
        ORDER BY 2, 4 desc;
    '''
]

create_table_sql = f'''
    create table if not exists {table_name}
    (
        "Id"                  bigint,
        "VendorID"            bigint,
        tpep_pickup_datetime  text,
        tpep_dropoff_datetime text,
        passenger_count       double precision,
        trip_distance         double precision,
        "RatecodeID"          double precision,
        store_and_fwd_flag    text,
        "PULocationID"        bigint,
        "DOLocationID"        bigint,
        payment_type          bigint,
        fare_amount           double precision,
        extra                 double precision,
        mta_tax               double precision,
        tip_amount            double precision,
        tolls_amount          double precision,
        improvement_surcharge double precision,
        total_amount          double precision,
        congestion_surcharge  double precision,
        airport_fee           double precision
    );
'''


import_csv_sql = f'''
    COPY {table_name}("Id", "VendorID", tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, "RatecodeID", 
              store_and_fwd_flag, "PULocationID", "DOLocationID", payment_type, fare_amount, extra, mta_tax, tip_amount, 
              tolls_amount, improvement_surcharge, total_amount, congestion_surcharge, airport_fee)
    FROM STDIN 
    DELIMITER ','
    CSV HEADER;
'''


drop_table_sql = f'DROP TABLE if exists {table_name}'
