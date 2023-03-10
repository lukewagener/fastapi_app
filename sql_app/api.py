from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'gryd_dev',
    'password': 'password',
    'database': 'gryd_db'
}

# Connect to the database
conn = pymysql.connect(**db_config)

def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

@app.get('/', tags=["root"])
async def read_root() -> dict:
    return {"msg": "Hello World"}

# GET using Database
@app.get('/properties')
async def get_properties():
        query = 'SELECT * FROM properties'
        result = execute_query(query)
        return result