from sqlalchemy.pool import NullPool
from sqlalchemy import (
    create_engine, 
    insert,
    select
)
from sqlalchemy.sql import text as sql_text
from sqlalchemy.orm import Session
from sqlalchemy import Column
from flask import current_app
import Models

class DatabaseManager:

    engine = None

    def __init__(self, configs):
        db_host = configs.get_config('DATABASE', 'host')
        username = configs.get_config('DATABASE', 'username')
        password = configs.get_config('DATABASE', 'password')
        database_name = configs.get_config('DATABASE', 'database')

        self.connection_string = f"mysql+pymysql://{username}:{password}@{db_host}/{database_name}"

    def create_engine(self):
        self.engine = create_engine(self.connection_string, poolclass=NullPool)

    def get_connection_pool(self):
        if not self.engine:
            self.create_engine()
        return self.engine

    def save_model_record(self, model, data, conn, uniq_key=None):
        data = {keys:values for keys, values in data.items() if values is not None}
        index_elements_list = [uniq_key] if uniq_key else data.keys()
        current_app.logger.info("Loading model %r,  data %r" % (model, data))
        record = conn.execute(model.__table__.insert().prefix_with('IGNORE'), data)
        if record:
            _id = record.inserted_primary_key[0] if  record.inserted_primary_key else None
        if not _id:
            stmt = select(model)
            if uniq_key:
                stmt = stmt.where(getattr(model, uniq_key) == data[uniq_key])
            else:
                for k in data.keys():
                    stmt = stmt.where(getattr(model, k) == data[k])
            result  =  conn.execute(stmt)

            _id = result.fetchone()["_id"]

        return _id

    def save_records(self, item):

        with self.get_connection_pool().connect() as conn:
            trans = conn.begin()
            try:
                geo_location_id  = None
                g_locaction =  item.get('_geolocation')
                if g_locaction and g_locaction[0] and g_locaction[1]:
                    geo_location = {
                      "latitude":g_locaction[0],
                      "longitude":g_locaction[1]
                    }
                    geo_location_id= self.save_model_record(
                        Models.Geolocation, 
                        geo_location, 
                        conn
                    )

                location = {
                    "unique_id":item.get("sec_a/unique_id"),
                    "biz_country_name":item.get("sec_a/cd_biz_country_name"),
                    "biz_region_name":item.get("sec_a/cd_biz_region_name"),
                    "geolocation_id":geo_location_id,
                }

                location_id= self.save_model_record(
                    Models.Location, 
                    location, 
                    conn,
                    "unique_id"
                )

                group = {
                    "biz_status":item.get("group_mx5fl16/cd_biz_status"),
                    "biz_operating":item.get("group_mx5fl16/bd_biz_operating") or ''
                }
                group_id= self.save_model_record(
                    Models.BusinessGroup, 
                    group, 
                    conn
                )

                business = {
                    "bda_name": item.get("sec_b/bda_name"),
                    "cohort": item.get("sec_b/cd_cohort"),
                    "program": item.get("sec_b/cd_program"),
                    "group_id": group_id,
                    "location_id": location_id,
                }
                business_id= self.save_model_record(
                    Models.Business, 
                    business, 
                    conn,
                    "bda_name"
                )
                client = {
                    "client_name": item.get("sec_c/cd_client_name"),
                    "client_id_manifest": item.get("sec_c/cd_client_id_manifest"),
                    "location": item.get("sec_c/cd_location"),
                    "clients_phone": item.get("sec_c/cd_clients_phone"),
                    "clients_phone_smart_feature": item.get("sec_c/cd_clients_phone_smart_feature"),
                    "gender": item.get("sec_c/cd_gender"),
                    "age": item.get("sec_c/cd_age"),
                    "nationality": item.get("sec_c/cd_nationality"),
                    "strata": item.get("sec_c/cd_strata"),
                    "disability": item.get("sec_c/cd_disability"),
                    "education": item.get("sec_c/cd_education"),
                    "client_status": item.get("sec_c/cd_client_status"),
                    "sole_income_earner": item.get("sec_c/cd_sole_income_earner"),
                    "howrespble_pple": item.get("sec_c/cd_howrespble_pple"),
                    "business_id": business_id,
                }
                client_id= self.save_model_record(
                    Models.Client, 
                    client, 
                    conn,
                    "client_id_manifest"
                )
                asset = {
                   "formhub_uuid":item.get("formhub/uuid") ,
                   "starttime": item.get("starttime"),
                   "endtime": item.get("endtime"),
                   "cd_survey_date": item.get("cd_survey_date"),
                   "_status": item.get("_status"),
                   "_submission_time": item.get("_submission_time"),
                   "__version__": item.get("__version__"),
                   "meta_instance_id": item.get("meta/instanceID"),
                   "_xform_id_string": item.get("_xform_id_string"),
                   "_uuid": item.get("_uuid"),
                   "_validation_status": item.get("_validation_status"),
                   "attachments": item.get("_attachments"),
                   "notes": item.get("_notes"),
                   "tags": item.get("_tags"),
                   "submitted_by": item.get("_submitted_by"),
                   "business_id":business_id,
                }

                asset_id= self.save_model_record(
                    Models.Asset, 
                    asset, 
                    conn,
                    "_uuid"
                )
            except:
                trans.rollback()
                raise
            else:
                trans.commit()
            return True


