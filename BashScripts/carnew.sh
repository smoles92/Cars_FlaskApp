#!/bin/bash

chmod u+x carnew.sh
curl -d '{"make":"Seat","model":"Cordoba", "year":"2003"}' -H "Content-Type:application/json" -X POST http://localhost:5000/car/new/