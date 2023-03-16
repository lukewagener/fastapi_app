# fastapi_app
Little Python app I cooked up using FastAPI/SQLAlchemy/Pymysql 
to connect to a dummy database of parking spots.

# DB
Using PhpMyAdmin via XAMPP, set up a database matching the credentials in 'database.py'
and import the .CSV file attached to create the 'spots' table.

# Run
To run, set up your virtual env (venv) in the root, 
then enter the command 'pip install uvicorn pymysql sqlalchemy fastapi' to install the 
necessary packages.

Then enter command 'uvicorn main:app --reload' to start the FastAPI service.

Then visit 'http://localhost:8000/docs' to test the endpoints.
