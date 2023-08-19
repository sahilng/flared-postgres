from flask import Flask, jsonify
import redis
import json

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    json_data = redis_client.get("my_key")
    if json_data:
        data = json.loads(json_data.decode("utf-8"))
        return jsonify(data)
    else:
        return jsonify({"error": "Data not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')