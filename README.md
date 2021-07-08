# Future-of-Work
Our goal is to create an application that analyzes the inflow and outflow of personnel and creates fancy, useful visualizations. 

### Running the API

You'll need [Docker](https://docs.docker.com/get-docker/) installed.

To build the app for the first time, or after a configuration change, run:
```
docker-compose up --build
```

Afterwards, you can just run
```
docker-compose up
```

Changes to your python code won't need a server restart, it'll work when you save your file.

The API will run on port 4000 by default. You can make requests to http://localhost:4000/api/hello to test if it is working.
