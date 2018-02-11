# Flask - Vue Boilerplate
Simple boiler plate project built with vue and bootstrap frontend, flask backend.

## To start the backend (Flask):
> cd backend
>  FLASK_APP=run.py FLASK_DEBUG=1 flask run 

## To start the frontend (Vue):
> cd frontend
> npm start

## Viewing the already existing pages:
* Vue Basic Homepage - http://localhost:8080/#/
* Vue Ranndom number Reading from api (Flask must be running) - http://localhost:8080/#/hi
* Flask Random Num generator - http://localhost:5000/api/random

## Accessing Frontend through flask:
Run the following the frontend folder (It will generate a dist folder which flask will read from)
> npm build

#### With flask running
* Vue Basic Homepage - http://localhost:5000/#/
* Homepage using flask api - http://localhost:5000/#/hi


