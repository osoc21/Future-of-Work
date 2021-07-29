from flask import Flask, make_response, jsonify, flash
from flask_restful import Api, Resource, reqparse, request, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
import werkzeug
import os
#For documentation
from flasgger import Swagger
#Database
import redis
#Our files
from database import writeCSVs,readCSVs,writeSupplyCSVs,readSupplyCSVs,writeDemandCSV,readDemandCSV, writeDemandParameter, getDemandParameter, setParameter, getParameter
from supply import calculateSupplyTitle,jobFamilyTitle
from demand import extractInfoFormulas,getFormulas,calculateDemand
from gap import calculateGap

template = {
  "swagger": "2.0",
  "info": {
    "title": "Flask Restful - Future of work",
    "description": "The API for the project for Deloitte called future of work.",
    "version": "1.0.0",
    "contact": {
      "name": "Erinn",
      "email": "evdsande@protonmail.com",
    }
  }
}

UPLOAD_FOLDER = '/'

def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'My API',
        'uiversion': 3,
        "specs_route": "/swagger/"
        }

    CORS(app,supports_credentials=True)
    
    r = redis.Redis(host='database',port=6379)
    
    swagger = Swagger(app, template= template)

    #Local Functions
    def allowed_file(filename,allowedextensions):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowedextensions
    FLASK_SECRET = os.getenv('FLASK_SECRET')
    app.secret_key = FLASK_SECRET if FLASK_SECRET else "StupidSecret"
    
    api = Api(app)

    #API calls
    class UploadAll(Resource):
        def post(self):
            """
            Upload 4 csv files to the server
            ---
            tags:
                - All
            parameters:
                - name: Population
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the current population
                - name: Attrition
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containting the attrition rates
                - name: Retirement
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the retirement age 
                - name: Demand
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the demand formulas 
            responses:
                405:
                    description: form is incorrect format could not find poplation file
                401:
                    description: form is incorrect format could not find attrition file
                402:
                    description: form is incorrect format could not find retirement file
                410:
                    description: population file is empty so no file was selected
                411:
                    description: attrition file is empty so no file was selected
                420:
                    description: population file isn't a csv
                421:
                    description: attrition file isn't a csv
                422:
                    description: retirement file isn't a csv
                200:
                    description: ok
                500:
                    description: internal server error
            """
            # check if the post request has the file part 
            if 'population' not in request.files:
                flash('population is missing')
                abort(400,message="form is incorrect format could not find population, files found:" + str(request.files.keys()))
            elif 'attrition' not in request.files:
                flash('attrition is missing')
                abort(401,message="form is incorrect format could not find attrition file, files found:" + str(request.files.keys()))
            elif 'retirement' not in request.files:
                flash('retirment is missing')
                abort(402,message="form is incorrect format could not find retirement file, files found:" + str(request.files.keys()))
            elif 'demand' not in request.files:
                flash('demand is missing')
                abort(402,message="form is incorrect format could not find demand file, files found:" + str(request.files.keys()))
            else:
                populationFile = request.files['population']
                attritionFile = request.files['attrition'] 
                retirementFile = request.files['retirement'] 
                demandFile = request.files['demand']
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
                if populationFile.filename == '':
                    flash('No Population file selected')
                    abort(410,message="population file is empty so no file was selected")
                elif attritionFile.filename == '':
                    flash('No Attrition file selected')
                    abort(411,message ="attrition file is empty so no file was selected")
                elif retirementFile.filename == '':
                    flash('No Retirement file selected')
                    abort(412,message="retirement file is empty so no file was selected")
                elif demandFile.filename == '':
                    flash('No Demand file selected')
                    abort(412,message="demand file is empty so no file was selected")
                elif populationFile and attritionFile and retirementFile and demandFile:
                    if not(allowed_file(populationFile.filename,{'csv'})):
                        flash('population is not a csv')
                        abort(420,message="population file is not a csv")
                    elif not(allowed_file(attritionFile.filename,{'csv'})):
                        flash('attrition is not a csv')
                        abort(421,message="attrition file is not a csv")
                    elif not(allowed_file(retirementFile.filename,{'csv'})):
                        flash('retirement is not a csv')
                        abort(422,message="retirement file is not a csv")
                    elif not(allowed_file(demandFile.filename,{'csv'})):
                        flash('demand is not a csv')
                        abort(422,message="demand file is not a csv")
                    else: 
                        globalID = writeCSVs([populationFile,attritionFile,retirementFile],["population","attrition","retirement"],demandFile,r)
                        data = extractInfoFormulas(getFormulas(readDemandCSV(globalID,r))) 
                        writeDemandParameter(globalID,list(data["parameters"]),0,r)
                        resp = make_response(readCSVs(globalID,r))
                        resp.set_cookie('globalID', globalID,max_age=100000000,samesite='Lax')
                        return resp
                else: 
                    flash('Internal Error')
                    abort(500,message="and failed") 

    class LoadAll(Resource): 
        def get(self):
            """
            get back all the data you have uploaded
            ---
            tags:
                - All
            responses:
                200: 
                    description: succes returns the data as a json
                405:
                    description: couldn't find the globalID cookie
            """
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                resp = make_response(readCSVs(globalID,r))
                return resp
            else:
                abort(405,message="Couldn't find ID")


    class UploadSupply(Resource):
        def post(self):
            """
            Upload supply csv files to the server and get a JSON back with UUID
            ---
            tags:
                - Supply
            parameters:
                - name: Population
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the current population
                - name: Attrition
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containting the attrition rates
                - name: Retirement
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the retirement age 
            responses:
                405:
                    description: form is incorrect format could not find poplation file
                401:
                    description: form is incorrect format could not find attrition file
                402:
                    description: form is incorrect format could not find retirement file
                410:
                    description: population file is empty so no file was selected
                411:
                    description: attrition file is empty so no file was selected
                420:
                    description: population file isn't a csv
                421:
                    description: attrition file isn't a csv
                422:
                    description: retirement file isn't a csv
                200:
                    description: succes returns a global ID where the files are stored
                500:
                    description: internal server error
            """
            # check if the post request has the file part
            if 'population' not in request.files:
                flash('population is missing')
                abort(400,message="form is incorrect format could not find population, files found:" + str(request.files.keys()))
            elif 'attrition' not in request.files:
                flash('attrition is missing')
                abort(401,message="form is incorrect format could not find attrition file, files found:" + str(request.files.keys()))
            elif 'retirement' not in request.files:
                flash('Retirment is missing')
                abort(402,message="form is incorrect format could not find retirement file, files found:" + str(request.files.keys()))
            else:
                populationFile = request.files['population']
                attritionFile = request.files['attrition']
                retirementFile = request.files['retirement'] 
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
                if populationFile.filename == '':
                    flash('No Population file selected')
                    abort(410,message="population file is empty so no file was selected")
                elif attritionFile.filename == '':
                    flash('No Attrition file selected')
                    abort(411,message ="attrition file is empty so no file was selected")
                elif retirementFile.filename == '':
                    flash('No Retirement file selected')
                    abort(412,message="attrition file is empty so no file was selected")
                elif populationFile and attritionFile and retirementFile:
                    if not(allowed_file(populationFile.filename,{'csv'})):
                        flash('population is not a csv')
                        abort(420,message="population file is not a csv")
                    elif not(allowed_file(attritionFile.filename,{'csv'})):
                        flash('attrition is not a csv')
                        abort(421,message="attrition file is not a csv")
                    elif not(allowed_file(retirementFile.filename,{'csv'})):
                        flash('retirement is not a csv')
                        abort(422,message="retirement file is not a csv")
                    else: 
                        globalID = writeSupplyCSVs([populationFile,attritionFile,retirementFile],["population","attrition","retirement"],r)
                        resp = make_response({"succes":"succes"})
                        resp.set_cookie('globalID', globalID,max_age=100000000,samesite='Lax')
                        return resp
                else:
                    flash('Internal Error')
                    abort(500,message="and failed") 

    class LoadSupply(Resource): 
        def get(self):
            """
            get back the supply data you have uploaded
            ---
            tags:
                - Supply
            responses:
                200:
                    description: succes returns the data as a json
                405:
                    description: couldn't find the globalID cookie
            """ 
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                resp = make_response(readSupplyCSVs(globalID,r))
                return resp
            else:
                abort(405,message="Couldn't find ID")

    class CalculateSupply(Resource):
        def get(self):
            """
            get back the data you have uploaded
            ---
            tags:
                - Supply
            responses:
                200:
                    description: succes returns the data as a json
                405:
                    description: couldn't find the globalID cookie
            """
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                supply = calculateSupplyTitle(readSupplyCSVs(globalID,r))
                resp = make_response(jsonify(supply))
                return resp
            else:
                abort(405,message="Couldn't find ID")

    class UploadDemand(Resource):
        def post(self):
            """
            Upload the csv for the demand
            ---
            tags:
                - Demand
            parameters:
                - name: Population
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the current population
                - name: Attrition
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containting the attrition rates
                - name: Retirement
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the retirement age 
                - name: Demand
                  in: files
                  type: csv file
                  required: true
                  description: a csv-file containing the demand formulas 
            responses:
                405:
                    description: form is incorrect format could not find poplation file
                401:
                    description: form is incorrect format could not find attrition file
                402:
                    description: form is incorrect format could not find retirement file
                410:
                    description: population file is empty so no file was selected
                411:
                    description: attrition file is empty so no file was selected
                420:
                    description: population file isn't a csv
                421:
                    description: attrition file isn't a csv
                422:
                    description: retirement file isn't a csv
                200:
                    description: ok
                500:
                    description: internal server error
            """
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                if 'demand' not in request.files:
                    flash('demand is missing')
                    abort(400,message="form is incorrect format could not find demand, files found:" + str(request.files.keys()))
                else:
                    demandFile = request.files['demand']   
                    if demandFile.filename == '':
                        flash('No demand file selected')
                        abort(410,message="demand file is empty so no file was selected")
                    elif demandFile and allowed_file(demandFile,allowedextensions={'csv'}):
                        writeDemandCSV(globalID,demandFile,r)
                        resp = make_response()
                        return resp
                    else:
                        abort(500)
            else:
                abort(405,message="Couldn't find ID")
    

    class LoadDemand(Resource): 
        def get(self):
            """
            get back the demand data
            ---
            tags:
                - Demand
            responses:
                200:
                    description: succes returns the data as a json
                405:
                    description: couldn't find the globalID cookie
            """ 
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                resp = make_response(readDemandCSV(globalID,r))
                return resp
            else:
                abort(405,message="Couldn't find ID")

    class Parameters(Resource):
        def get(self):
            """
            get back the parameters from the demand data
            ---
            tags:
                - Demand
                - Parameter
            parameters:
                - name: year
                  type: int
                  required: true
                  description: the year
                - name: id
                  type: string
                  required: true
                  description: the id of the row
            responses:
                200:
                    description: succes returns the parameters
                405:
                    description: couldn't find the globalID cookie
            """ 
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                result = getDemandParameter(globalID,r)
                resp = make_response(jsonify(result))
                return resp
            else:
                abort(405,message="Couldn't find ID")
    
    class Parameter(Resource):
        def patch(self,year,id):
            """
            get back the parameters from the demand data
            ---
            tags:
                - Demand
                - Parameter
            responses:
                200:
                    description: succes
                405:
                    description: couldn't find the globalID cookie
            """ 
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID") 
                body = eval(request.data) 
                setParameter(id,year,body["parameter"],r)
                resp = make_response({"result":"result"})
                return resp
            else:
                abort(405,message="Couldn't find ID")

    class CalculateDemand(Resource):
        def get(self):
            """
            get back the demand calculation
            ---
            tags:
                - Demand
            responses:
                200:
                    description: succes returns the result of the calculation
                405:
                    description: couldn't find the globalID cookie
            """ 
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID") 
                result = calculateDemand(readDemandCSV(globalID,r),getParameter(globalID,r),jobFamilyTitle(readSupplyCSVs(globalID,r)))
                resp = make_response(jsonify(result))
                return resp
            else:
                abort(405,message="Couldn't find ID")
            

    class CalculateGap(Resource):
        def get(self):
            """
            get back the gap calculation
            ---
            tags:
                - Gap
            responses:
                200:
                    description: succes returns the result of the calculation
                405:
                    description: couldn't find the globalID cookie
            """
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID") 
                
                supply = calculateSupplyTitle(readSupplyCSVs(globalID,r))

                demand = calculateDemand(readDemandCSV(globalID,r),getParameter(globalID,r),jobFamilyTitle(readSupplyCSVs(globalID,r)))
                
                result = calculateGap(supply,demand)
                resp = make_response(jsonify(result))
                return resp
            else:
                abort(405,message="Couldn't find ID")

    # API resource routing
    # All
    api.add_resource(UploadAll, "/api/all/upload/")
    api.add_resource(LoadAll, "/api/all/load/")
    # Supply
    api.add_resource(UploadSupply, "/api/supply/upload/")
    api.add_resource(LoadSupply, "/api/supply/load/")
    api.add_resource(CalculateSupply, "/api/supply/calculate/") 
    # Demand
    api.add_resource(UploadDemand, "/api/demand/upload/")
    api.add_resource(LoadDemand, "/api/demand/load/")
    api.add_resource(Parameters, "/api/demand/parameters/")
    api.add_resource(Parameter, "/api/demand/parameter/<string:year>/<string:id>/")
    api.add_resource(CalculateDemand, "/api/demand/calculate/")
    # Gap
    api.add_resource(CalculateGap, "/api/gap/calculate/")

    return app