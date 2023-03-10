from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql

app = FastAPI()

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'gryd_dev',
    'password': 'password',
    'database': 'gryd_db'
}

# Connect to the database
conn = pymysql.connect(**db_config)