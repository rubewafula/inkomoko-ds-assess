from flask_restful import Resource
from flask import (
    current_app,
    request
)

import requests
import json
from ConfigLoader import Config
import ijson
from Db import DatabaseManager
import Models

class ExtractAndSaveData(Resource):

    def stream_json_data(self, url, headers, payload):
        response = requests.get(url, headers=headers, data=payload, stream=True)
        response.raise_for_status() 
        return response.raw  

    def process_item_data(self, item):
        db_manager = DatabaseManager(self.configs)
        db_manager.save_records(item)


    def process_and_save_json(self, url, headers, payload):
        response = requests.get(url, headers=headers, data=payload, stream=True)
        #response.raise_for_status() 
        json_response = response.json()
        try:
            #for item in ijson.items(response.raw, 'results.item', use_float=True, buf_size=1024):
            for item in json_response.get("results"):
                current_app.logger.info("Fetching raw json dict: %r" % item)
                self.process_item_data(item)
        except ijson.JSONError as e:
            print(f"JSON parsing error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return {"status":0, "Message":"Message processed OK"}

    def get(self):
        self.configs = Config()
        url  = self.configs.get_config('DATAEXTRACTION', 'url')
        lang = self.configs.get_config('DATAEXTRACTION', 'language')
        token = self.configs.get_config('DATAEXTRACTION', 'token')

        payload = ""
        headers = {
            'Authorization': 'Token {}'.format(token),
            'Cookie': 'django_language={}'.format(lang)
        }
        #Will use stream to help manage large file
        current_app.logger.info("Calling process json get data from API")
        result = self.process_and_save_json(url, headers, payload)

        return result

class AcceptAndSaveData(Resource):

    def get_data(self):
        return request.get_json(force=True)

    def process_and_save_post_data(self, data):
        db_manager = DatabaseManager(self.configs)
        db_manager.save_records(data)

    def post(self):
        data =  self.get_data()
        self.configs = Config()
        url  = self.configs.get_config('DATAEXTRACTION', 'url')
        lang = self.configs.get_config('DATAEXTRACTION', 'language')
        token = self.configs.get_config('DATAEXTRACTION', 'token')

        result = self.process_and_save_post_data(data)

        return {"status":200, "message":"Nothing get", "data":data}

class RegisterWebHook(Resoure):
    def get(self):
        self.configs = Config()
        url  = self.configs.get_config('WEBHOOK', 'url')
        callback = self.configs.get_config('WEBHOOK', 'callback')
        payload = json.dumps({"url": callback})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.json()
