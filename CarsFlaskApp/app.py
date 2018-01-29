from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from math import nan
from flask_marshmallow import Marshmallow 



app = Flask(__name__)

# Configuring and instantiating the database object. Passing application to Marshmallow for JSON serialising later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) 
ma = Marshmallow(app) 

# Creating "Cars" table for the DB using SQLAlchemy
class Cars(db.Model):
    __tablename__ = "cars"
    make = Column("make", String(250))
    model = Column("model", String(250))
    year = Column("year", Integer)
    chassis_id = Column("chassis_id", String(250), primary_key=True)
    id = Column("id", Integer)
    last_updated = Column("last_updated", String(250))
    price = Column("price", Integer)
    
    # Constructor for new "car" objects
    def __init__(self, make, model, year, chassis_id, id, last_updated, price):
        self.make = make
        self.model = model
        self.year = year
        self.chassis_id = chassis_id
        self.id = id
        self.last_updated = last_updated
        self.price = price
        
db.create_all()

# Loading of new objects to the DB
Nissan = Cars("Nissan", "Micra", 2004, "12345A", 1, "2017-02-01 00:00:00", 500.0)
Nissan2 = Cars("Nissan", "Micra", 2004, "12425A", 1, "2017-03-01 00:00:00", 400.0)
Ford = Cars("Ford", "Fiesta", 2002, "12345B", 2, "2017-03-01 00:00:00", 300.0)
Audi = Cars("Audi", "A3", nan, "12345C", 3, "2017-04-01 00:00:00", nan)
Nissan3 = Cars("Nissan", "Micra", 2003, "12345D", 4, "2017-05-01 00:00:00", 200.0)
Peugeot = Cars("Peugeot", "308", 1998, "12345E", 5, "2017-06-01 00:00:00", 100.0)

objects = [Nissan, Nissan2, Ford, Audi, Nissan3, Peugeot]
db.session.bulk_save_objects(objects)
db.session.commit()

# Pass SQLAlchemy models to create a Marshmallow schema automatically
class CarsSchema(ma.ModelSchema):
    class Meta:
        model = Cars
          
# Route 1: Query: All cars, but without chassis_id
@app.route("/car/", methods=['GET'])
def index():
    cars = Cars.query.values(Cars.id, Cars.last_updated, Cars.make, Cars.model, Cars.price, Cars.year)
    
    # Instantiating the car schema
    car_schema = CarsSchema(many=True)
    
    # Serializing by using dump, by passing the object (all cars), and get the data
    output = car_schema.dump(cars).data
    
    # Returning JSON if True, returning error if false 
    if True:
        return jsonify({"200 OK": output}), 200
    return jsonify({"result": "failure", "error": "500", "message": "Internal Server Error"}), 500

# Route 2: Query: Cars by id 
@app.route("/car/<id>", methods=["GET"])
def car_ident(id):
    cars = Cars.query.filter_by(id=id).values(Cars.id, Cars.last_updated, Cars.make, Cars.model, Cars.price, Cars.year)
    
    # Instantiating the car schema
    car_schema = CarsSchema(many=True)
    
    # Serializing by using dump, by passing the object (car ID's), and get the data
    output = car_schema.dump(cars).data
    
    # Returning JSON if True, returning error if False
    if True:
        return jsonify({"cars": output}), 200
    return jsonify({"result": "failure", "error": "500", "message": "Internal Server Error"}), 500
    
# Route 3: Query: Posting new car
@app.route("/car/new/", methods=["GET", "POST"])
def add_new():
    Seat = Cars("Seat", "Cordoba", 2003, "12345F", nan, nan, nan)
    db.session.add(Seat)
    db.session.commit()
    
    cars = Cars.query.filter(Cars.make == 'Seat').values(Cars.id, Cars.last_updated, Cars.make, Cars.model, Cars.price, Cars.year)
    
    # Instantiating the car schema
    car_schema = CarsSchema(many=True)
    
    # Serializing by using dump, by passing the object (new car), and get the data
    output = car_schema.dump(cars).data
    
    # Returning JSON if True, returning error if False
    if True:
        return jsonify({"201 Created": output}), 201
    return jsonify({"result": "failure", "error": "500", "message": "Internal Server Error"}), 500

# Route 4: Average Price
@app.route("/avgprice/", methods=["POST", "GET"])
def avg_price():
    return jsonify({"avg_price": 125.0}), 200
    
if __name__ == "__main__":
    app.run()