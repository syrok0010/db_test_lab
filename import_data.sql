create table taxi
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

COPY taxi("Id", "VendorID", tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, "RatecodeID", store_and_fwd_flag, "PULocationID", "DOLocationID", payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, congestion_surcharge, airport_fee)
FROM '/tmp/nyc_yellow_tiny.csv'
DELIMITER ','
CSV HEADER;