# GRYDBackend Technical Manual

-WI2023 term ACE team used Xampp/phpMyAdmin to manage the MySQL database (locally)

# ~ Terminologies

DB - short for database

Spots - pins / markers; can also mean the first table in the database

Zones - selected spot, pin, or marker (on the map); can also mean the second table in the database

# A. Getting Started

a1. open the Xampp control panel and start the Apache & MySQL modules

a2. go to http://localhost:31337/phpmyadmin/index.php

# B. Database Setup

b1. create a db named 'gryd_db'

b2. run the 'gryd_db.sql' script to create the tables and insert data automatically

b3. create new credentials using these items:
    user: gryd_dev,
    host: localhost,
    password: password

# ~ Optional Database Customization

- if you wish to change any of the database credentials/setup, make sure you alter the db connection string found inside 'database.py' file

- if you wish to change the table names, fields, etc. of the data, make sure to also alter the models and schema found in 'models.py' and 'schema.py' files

# C. API/Backend Initialization

c1. before initializing the backend, make sure that you have these packages installed in your project repo (e.g. pip install "package name"):
    fastapi,
    uvicorn,
    pymysql,
    sqlalchemy

c2. initialize the API/Backend by running the Apache & MySQL modules in the Xampp control panel

c3. inside the terminal, enter and run 'python main.py' command

# D. Check API Endpoints

d1. visit http://localhost:8000/docs to view and test API endpoints

d2. alternatively, you can also check the data via typing in the specific endpoint you want to check inside your browser's address bar (refer to the 'api.py' file to view the URL endpoints)

# ~ Recommendations/Suggestions

- using 'Git Bash' as the primary terminal is a better option for running commands; most especially installing or running python-related files or packages

- when using Visual Studio Code text editor, the 'Thunder Client' extension, published by Ranga Vadhineni is a great tool to check data via API endpoints

