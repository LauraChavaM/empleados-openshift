import os, time
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient(os.environ["MONGO_URI"])

@app.post("/escribir")
def escribir():
    body = request.get_json(silent=True) or {}
    t0 = time.perf_counter()
    coll = client[os.environ["DB_NAME"]][os.environ["COLLECTION_NAME"]]
    coll.insert_one({"nombre": body.get("nombre"), "salario": body.get("salario")})
    ms = round((time.perf_counter() - t0) * 1000, 2)
    return jsonify(ok=True, tiempo_db_ms=ms)