from flask import Flask
from flask_restful import Api, Resource
import os
import json

app = Flask(__name__)
api = Api(app)


class API(Resource):
    @staticmethod
    def get():
        with open(os.path.join(os.path.dirname(__file__), "questionable.json")) as f:
            data = json.load(f)
        return data


api.add_resource(API, "/<string:question>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3996)

