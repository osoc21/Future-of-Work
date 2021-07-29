# Future-of-Work
Our goal is to create an application that analyzes the inflow and outflow of personnel and creates fancy, useful visualizations.  

## Backend

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

The API will run on port 4000 by default. 

### Endpoints

| family | name | path | input | output |
|---|---|---|---|---|
| All | upload all files | ```/api/all/upload/``` | files should contain attrition.csv, demand.csv, population.csv and retirement.csv | 200 OK + cookie with unique identifier |
|  | load all files | ```/api/all/load/``` | need a cookie with the unique identifier assigned by the API | JSON : {attrition: [{rowID:row}, ...],population:[{rowID:row},...],retirement:[{rowID:row},...],demand:[{rowID:row},...]} |
| Supply | upload supply | ```/api/supply/upload/``` | files should contain attrition.csv, population.csv and retirement.csv | 200 OK + cookie with unique identifier |
|  | load supply files |``` /api/supply/load/``` | need a cookie with the unique identifier assigned by the API | JSON : {attrition: [{rowID:row}, ...],population:[{rowID:row},...],retirement:[{rowID:row},...]} |
|  | calculate result from supply | ```/api/supply/calculate/``` | need a cookie with the unique identifier assigned by the API | JSON : [{"year":year,"data":{family:[{job:FTE},...],...}},...] |
| Demand | upload demand files | ```/api/demand/upload/``` | files should contain demand.csv + there should be a cookie | 200 OK |
|  | load demand file | ```/api/demand/load/``` | need a cookie with the unique identifier assigned by the API | JSON : {demand:[{rowID:row},...]} |
|  | values for each parameter | ```/api/demand/parameters/``` | need a cookie with the unique identifier assigned by the API | JSON : [{"name":parameter,"data":[{"id":id,"year":year,"parameter":parameter},...]},...] |
|  | Change value of one parameter | ```/api/demand/parameter/*year*/*id*/``` | need a cookie with the unique identifier assigned by the API | 200 OK |
|  | calculate result from demand | ```/api/demand/calculate/``` | need a cookie with the unique identifier assigned by the API | JSON : [{"year":year,"data":{family:[{job:FTE},...],...}},...] |
| Gap | calculate result from gap | ```/api/gap/calculate/``` | need a cookie with the unique identifier assigned by the API | JSON : [{"year":year,"data":{family:[{job:FTE},...],...}},...] |

### Files

- api.py
    - contains the main api with all it's endpoints
- app.py
    - contains the app to run
- file_handling.py
    - contains the main functionality of interacting with the Redis data store
- supply.py
    - contains the main calculation of the supply side
- demand.py
    - contains the main calculation of the demand side
- gap.py
    - contains the main calculation of the gap side

## Frontend 

### Setting up the project

To install Svelte and all the dependencies, go to the fronend folder and run:
```
npm install
```
Afterwards, to start the app, run:
```
npm run dev
```

### File structure

In App.svelte you can find all the routes for the app.  
Inside the src folder, you can find folders for all the components, pages, stores and API calls.

## API

In the ```/api``` folder you can find all the functions for backend communication.

The **fetch** functions get called in the different providers (found in ```/components/providers```) so all the child components of the providers can access the fetched data.

The **patch** function is called in the Demand component (found in ```/components/demand```). This sends changes to the coefficients to the server.

The **upload** function is called in the upload page, this sends all the uploaded csv files to the server.  

## COMPONENTS

In the ```/components``` folder you can find all the components used in the app. the dataProviders components is where the API communication happens. If the provder does a fetch request, all the child components of the provder will have access to the data fetched by the provider.

In the ```/supply, /demand and /gap``` folders you can find the tables and charts with their corresponding data.

In the ```/layouts``` folder you can find two files, the ```HomeLayout.svelte``` is used for the landing page, and the ```AppLayout.svelte``` is used for the pages of the dashboard because this layout contains the side navigation.

## STORES

In the stores folder you can find all the writable datastores. Inside the dataProviders all the data gets fetched and gets stored in these stores. later this data is used in childcomponents to build the tables.

### Structure of the CSV files

The application expects 4 files to be uploaded at the start (**without all 4 files you can't proceed to the next steps**)

## Population file
| Job title | Job family | Country of Personnel Area | FTE | Birth date |
| --------- | ---------- | ------------------------- | --- | ---------- |

## Attrition file (country names can vary)
| Job family | Belgium | UK | Germany | US | China | Japan | Others | Global |
| ---------- | ------- | -- | ------- | -- | ------| ----- | ------ | ------ |

## Demand file
| Job title | Formula |
| --------- | ------- |

## Retirement file
| Country of Personnel Area | Age |
| ------------------------- | --- |
