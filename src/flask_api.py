from flask import Flask
from flask_restful import Api, Resource

from chatbot import Chatbot

app = Flask(__name__)
api = Api(app)

cb: Chatbot = Chatbot()


class API(Resource):
    @staticmethod
    def get(question):
        return {"data": cb.get_response(question)}


api.add_resource(API, "/<string:question>")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

