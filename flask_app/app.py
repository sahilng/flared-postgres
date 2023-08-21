from flask import Flask, jsonify
import redis
import json
import pandas as pd
from datetime import datetime, timezone, timedelta

from datetime import datetime, timezone, timedelta

def custom_strptime(date_str):
    base_date_str, offset = date_str[:-3], date_str[-3:]
    sign = 1 if offset[0] == '+' else -1
    offset = int(offset[1:])  # Convert the remaining part (e.g., '00') to an integer

    offset_delta = timedelta(hours=offset) * sign

    dt = datetime.strptime(base_date_str, '%Y-%m-%d %H:%M:%S.%f')
    dt = dt.replace(tzinfo=timezone(offset_delta))

    return dt

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    json_data = redis_client.get("my_key")
    if json_data:
        data = json.loads(json_data.decode("utf-8"))
        update_time = data['data'][0][0]
        update_time_dt = custom_strptime(update_time)
        update_time_human_readable = update_time_dt.strftime('%B %-d, %Y at %-I:%M:%S%p UTC')
        return "Redis last updated from Postgres at: <b>" + update_time_human_readable + "</b>"
    else:
        return "Data not found, refresh in a few moments."
    
@app.route('/api')
def api():
    json_data = redis_client.get("my_key")
    if json_data:
        data = json.loads(json_data.decode("utf-8"))
        return jsonify(data)
    else:
        return jsonify({"error": "Data not found, refresh in a few moments."}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')