# Optimized-Query
In Project of Database course, we try to optimize 6 queries with SQL Server

## About Project
This project contains CSV files about movies. The files include name, rating, score, tag, etc. (because the size is big, upload to Onedrive, you can download it).

We have 6 questions and should write queries and reduce time with Index, Non-cluster index, partition, etc. finally show result in simple flask project

## Files
*	Can see questions in: [Notes.pdf](Notes.pdf)
*	Can see queries in: [queries.sql](queries.sql)
*	Can see flask project: flask_project directory
*	Can see screenshots: screenshots directory
*	Can see full report: [Repot_Project1.pdf](Repot_Project1.pdf)

## Structure of Flask Project
* `Flask_Application.py` file is a controller file that maps address o suitable function and result
* `Data.py` file in this file we establish connection to SQL Server with `pyodbc` and execute queries.
* `Templates` directory contains HTML files.
* `Static` directory contains CSS and PNG files.


## Installing Tools
* flask
* [pyodbc](https://pypi.org/project/pyodbc/)
* SQL Server


## Run
Run `Flask_Application.py` and enter: localhost:4500/
enjoy it :)

