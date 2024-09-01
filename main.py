from flask import Flask
from flask_restful import Api
import logging

#custom class declaration

from DataAssignment import (
    ExtractAndSaveData, 
    AcceptAndSaveData
)

app = Flask(__name__)
api = Api(app)

api.add_resource(ExtractAndSaveData, '/vx/extract-data')
api.add_resource(AcceptAndSaveData, '/vx/accept/data')

log_formatter = logging.Formatter(
    "%(asctime)s %(levelname)-8s %(name)-5s %(filename)s:%(lineno)d:%("
    "funcName)-10s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

app.logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
app.logger.addHandler(handler)

if __name__ == '__main__':
    app.run(debug=True)

