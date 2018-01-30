# Cars_FlaskApp

## Project Description

This project implements a Python Flask API using Sqlite database. The project consists of two core folders:
1. **Cars_FlaskApp**
* app.py - The Flask application, separated by the required routes
* requirements.txt - A text file of all required environment imports to run the application
2. **Bash Scripts**
* *cars.sh* - Uses cURL to return JSON data for all cars information, without chassis_id 
* *car1.sh* - Uses cURL to return JSON data for cars based on id, without chassis_id
* *carnew.sh* - Uses cURL to post JSON data for a new car. After executing, the entry will appear in the "cars" route
* *avgprice.sh* - Uses cURL to post JSON average price

## Application execution
* Pull the repository files and open within an IDE (i.e. Eclipse), creating an environment if desired
* On the command-line within the environment, execute requirements.txt to 
install required imports: **_pip install -r /path/to/requirements.txt_**
* In the IDE or the command-line, execute the app.py file: **_python app.py_**
* This will create the database** and load the application on **http://127.0.0.1:5000**
* Changing the route structure **_"/car/"_**, **_"/car/1/"_**, **_"/car/new/"_**, **_"/avgprice/"_** will return the required data or an error

## Bash execution (cURL)
* The bash (_.sh_) scripts contain the required privledges to execute and retrieve the data.
* These can be executed on the unix command line - Example: user ~ **_./cars.sh_**

#### **Note: 
Once the _app.py_ file is executed, the database _database.db_, will be created in the current directory.
The loading of the database objects occurs within the app.py file, therefore should the _app.py_ file be executed subsequent times, the 
database should be deleted before these subsequent executions, to avoid clashes between keys by re-loading the same data. 
