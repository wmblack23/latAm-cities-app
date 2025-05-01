from flask import Flask, request, render_template, redirect, url_for, flash, session, make_response, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

# Connect to Mongo
clusterUrl = os.environ["clusterUrl"]
client = MongoClient(clusterUrl)
db = client['latAm-app']

application = Flask(__name__)
CORS(application)

@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    application.run(debug=True)