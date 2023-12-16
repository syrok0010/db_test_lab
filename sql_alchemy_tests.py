from library_tests import LibraryTests
from sqlalchemy.orm import Mapped, mapped_column, Session, DeclarativeBase
from sqlalchemy import create_engine, func
from sqlalchemy.types import TIMESTAMP
from config_loader import table_name, pg_password


class Base(DeclarativeBase):
    pass


class TaxiRide(Base):
    __tablename__ = table_name

    id: Mapped[int] = mapped_column(primary_key=True)
    VendorID: Mapped[int]
    tpep_pickup_datetime: Mapped[str]
    tpep_dropoff_datetime: Mapped[str]
    passenger_count: Mapped[float]
    trip_distance: Mapped[float]
    RatecodeID: Mapped[int]
    store_and_fwd_flag: Mapped[str]
    PULocationID: Mapped[int]
    DOLocationID: Mapped[int]
    payment_type: Mapped[int]
    fare_amount: Mapped[float]
    extra: Mapped[float]
    mta_tax: Mapped[float]
    tip_amount: Mapped[float]
    tolls_amount: Mapped[float]
    improvement_surcharge: Mapped[float]
    total_amount: Mapped[float]
    congestion_surcharge: Mapped[float]
    airport_fee: Mapped[float]


class SQLAlchemyTests(LibraryTests):
    def __init__(self):
        super().__init__()
        self.engine = None
        self.session = None

    def setup(self, path: str):
        self.engine = create_engine(f"postgresql+psycopg2://postgres:{pg_password}@localhost:5432/postgres")
        self.session = Session(self.engine)
        pass

    def query1(self):
        return (self.session
                .query(TaxiRide.VendorID, func.count(TaxiRide.VendorID))
                .group_by(TaxiRide.VendorID)
                .all()
                )

    def query2(self):
        return (self.session
                .query(TaxiRide.passenger_count, func.avg(TaxiRide.total_amount))
                .group_by(TaxiRide.passenger_count)
                .all()
                )

    def query3(self):
        return (self.session
                .query(
                    TaxiRide.passenger_count,
                    func.extract('Year', func.cast(TaxiRide.tpep_pickup_datetime, TIMESTAMP)).label('Year'),
                    func.count()
                )
                .group_by(TaxiRide.passenger_count, 'Year')
                .all()
                )

    def query4(self):
        return (self.session
                .query(
                    TaxiRide.passenger_count,
                    func.extract('Year', func.cast(TaxiRide.tpep_pickup_datetime, TIMESTAMP)).label('Year'),
                    func.round(TaxiRide.trip_distance),
                    func.count()
                    )
                .group_by(TaxiRide.passenger_count, 'Year', TaxiRide.trip_distance)
                .all()
                )

    def release(self):
        self.session.close()
        self.engine.dispose()
