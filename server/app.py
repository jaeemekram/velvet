from flask import Flask, request, jsonify, session, json
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from flask_restful import Api
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"




if __name__ == '__main__':
    app.run(debug=True)