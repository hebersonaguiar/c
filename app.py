import os
from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/": {"origins": ""}})
app.secret_key = "7pI.X7<w-qqE&a" 

@app.route("/")
def main():
    return "Boa noite FIAP! GitOps X ArgoCD"

@app.route("/health") 
def health():
    data = '{"health": "ok"}' 
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
