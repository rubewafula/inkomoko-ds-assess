from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db


Base = declarative_base()
metadata = Base.metadata

class Asset(Base):
    __tablename__ = "assets"

    _id =  db.Column(db.BigInteger, primary_key=True)
    formhub_uuid =  db.Column(db.String(43), nullable=False)
    starttime =   db.Column(db.DateTime, nullable=False)
    endtime =  db.Column(db.DateTime, nullable=False)
    cd_survey_date =  db.Column(db.Date, nullable=False)

    _status =  db.Column(db.String(25), nullable=False)
    _submission_time =  db.Column(db.DateTime, nullable=False)
    __version__ =  db.Column(db.String(35), nullable=False)
    meta_instance_id =  db.Column(db.String(55), nullable=False)
    _xform_id_string = db.Column(db.String(35), nullable=False)
    _uuid =  db.Column(db.String(43), nullable=False, unique=True)
    _validation_status = db.Column(db.JSON, nullable=True)

    attachments = db.Column(db.JSON, nullable=True)
    notes= db.Column(db.JSON, nullable=True)
    tags = db.Column(db.JSON, nullable=True)
    submitted_by = db.Column(db.String(60), nullable=True)
    business_id = db.Column(db.BigInteger, db.ForeignKey('businesses._id'))


    def __repr__(self):
        return f"<Asset {self.formhub_uuid}>"


class Location(Base):
    __tablename__ = 'locations';

    _id =  db.Column(db.BigInteger, primary_key=True)
    unique_id =  db.Column(db.String(45), nullable=False, unique=True)
    biz_country_name =  db.Column(db.String(34), nullable=False)
    biz_region_name =  db.Column(db.String(35), nullable=False)
    geolocation_id = db.Column(db.BigInteger, db.ForeignKey('geolocations._id'))


    def __repr__(self):
        return f"<Location {self.cd_biz_region_name} - {cd_biz_region_name}>"

class Business(Base):
    __tablename__ = 'businesses'

    _id =  db.Column(db.BigInteger, primary_key=True)
    bda_name =  db.Column(db.String(45), nullable=False, unique=True)
    cohort =  db.Column(db.String(35), nullable=False)
    program = db.Column(db.String(35), nullable=False)
    group_id = db.Column(db.BigInteger, db.ForeignKey('business_groups._id'))
    location_id = db.Column(db.BigInteger, db.ForeignKey('locations._id'))


    def __repr__(self):
        return f"<Business {self.bda_name}>"

class Client(Base):
    __tablename__ = "clients"

    _id =  db.Column(db.BigInteger, primary_key=True)
    client_name =  db.Column(db.String(45),nullable=False)
    client_id_manifest =  db.Column(db.String(45),nullable=False, unique=True)
    location =  db.Column(db.String(45),nullable=False)
    clients_phone =  db.Column(db.String(45),nullable=False)
    clients_phone_smart_feature =  db.Column(db.String(45),nullable=False)
    gender =  db.Column(db.String(45),nullable=False)
    age =  db.Column(db.String(45),nullable=False)
    nationality =  db.Column(db.String(45),nullable=False)
    strata =  db.Column(db.String(45),nullable=False)
    disability =  db.Column(db.String(45),nullable=False)
    education =  db.Column(db.String(45),nullable=False)
    client_status =  db.Column(db.String(45),nullable=False)
    sole_income_earner =  db.Column(db.String(45),nullable=False)
    howrespble_pple =  db.Column(db.Integer,nullable=False)
    business_id = db.Column(db.BigInteger, db.ForeignKey('businesses._id'))


    def __repr__(self):
        return f"<Clinet {self.cd_client_name}>"

class BusinessGroup(Base):
    __tablename__ = 'business_groups'

    _id =  db.Column(db.BigInteger, primary_key=True)
    biz_status =  db.Column(db.String(45), nullable=False)
    biz_operating =  db.Column(db.String(35), nullable=False)

    __table_args__ = (db.UniqueConstraint('biz_operating', 'biz_status', name='uix_status_operating'),)


    def __repr__(self):
        return f"<BusinessGroup {self.biz_status}>"


class Geolocation(Base):
    __tablename__ = 'geolocations'

    _id =  db.Column(db.BigInteger, primary_key=True)
    latitude =  db.Column(db.Float, nullable=True)
    longitude =  db.Column(db.Float, nullable=True)
    
    __table_args__ = (db.UniqueConstraint('latitude', 'longitude', name='uix_lat_long'),)

    def __repr__(self):
        return f"<Geolocation {self.latitude}, {self.longitude}>"


