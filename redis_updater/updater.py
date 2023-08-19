import redis
import psycopg2
import time
import os
import json
from datetime import datetime

REDIS_HOST = 'redis'
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'default_db')
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'user')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'pass')

def fetch_data():
    # Connect to your database
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASS
    )

    # Fetch data from your Postgres
    cur = conn.cursor()
    cur.execute("SELECT now()::text, * FROM my_table;")  # This is just an example, modify as needed
    data = cur.fetchall()
    
    # Convert data to JSON and include the last update time
    json_data = {
        'data': data
    }
    
    return json.dumps(json_data)

while True:
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
    json_data = fetch_data()
    if json_data:
        redis_client.set("my_key", json_data)
    time.sleep(10)  # Run every 10 seconds, adjust as needed
