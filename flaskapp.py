from flask import Flask,jsonify
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

store=[{'name':'Store1','items':[{'name':'Item1','price':4000}]}]

class Shop(Resource):
    def get (self,name):

        return jsonify(store)


api.add_resource(Shop,'/<string:name>')
if __name__=='__main__':
    app.run(debug=True)
