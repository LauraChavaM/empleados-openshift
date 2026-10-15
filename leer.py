import os, time
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient(os.environ["MONGO_URI"])

@app.get("/leer")
def leer():
    t0 = time.perf_counter()
    coll = client[os.environ["DB_NAME"]][os.environ["COLLECTION_NAME"]]
    docs = list(coll.find({}, {"_id": 0}))
    ms = round((time.perf_counter() - t0) * 1000, 2)
    return jsonify(ok=True, tiempo_db_ms=ms, data=docs)