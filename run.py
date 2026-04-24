import pymysql

import os
from dotenv import load_dotenv
from file_utils import parse_filename 
from sql_query import ORIENTATION_QUERY as orientation_query
load_dotenv()

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=3306,
    user=os.getenv("DB_USER"),
    password=os.getenv("PASSWORD"),
    database="argus",
    charset="utf8mb4"
)

filename = "1485392407.Thu.Jan.26_12_00_07.AEST.2017.goldcst.c5.snap.jpg"

parsed_name = parse_filename(filename=filename)

timestamp = parsed_name["timestamp"]
station_name = parsed_name["station"]
camera_number = parsed_name["camera_number"] 

params = station_name, camera_number, timestamp, timestamp, timestamp, timestamp, timestamp

with conn:
    with conn.cursor() as cur:
        cur.execute(orientation_query,params)
        tilt, roll, azimuth = (cur.fetchone())
        print(tilt, roll, azimuth)
