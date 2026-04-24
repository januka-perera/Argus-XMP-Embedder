import pymysql

import os
from dotenv import load_dotenv

load_dotenv()

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=3306,
    user=os.getenv("DB_USER"),
    password=os.getenv("PASSWORD"),
    database="argus",
    charset="utf8mb4"
)

with conn:
    with conn.cursor() as cur:
        cur.execute("SELECT DATABASE()")
        print(cur.fetchone())