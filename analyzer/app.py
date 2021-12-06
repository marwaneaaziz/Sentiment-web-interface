from flask import Flask, request
from flask_restful import Resource, Api 
import model

app = Flask(__name__)
api  = Api(app)


class Input_data(Resource): 
    
    def post (self):

        content = request.get_json(silent=True)
        txt = content["text"]
        scores =model.predict(txt)

        return scores

api.add_resource(Input_data,"/predict")

if __name__ == '__main__':
    app.run()
