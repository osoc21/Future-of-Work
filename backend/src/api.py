from flask import Flask, make_response, jsonify, flash, session
from flask_restful import Api, Resource, reqparse, request, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
import werkzeug
import os
#For documentation
from flasgger import Swagger, swag_from
#Database
import redis
#Our files
from FileHandling import writeCSVs,readCSV
from supply import calculateSupply


template = {
  "swagger": "2.0",
  "info": {
    "title": "Flask Restful - Future of work",
    "description": "The API for the project for Deloitte.",
    "version": "0.1.1",
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
    class UploadFile(Resource):
        def post(self):
            """
            Upload 3 csv files to the server and get a JSON back with UUID
            ---
            tags:
                - File upload
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
                400:
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
                elif populationFile and attritionFile and retirementFile and map(lambda x: allowed_file(x,{'csv'}),[populationFile,attritionFile,retirementFile]):
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
                        globalID = writeCSVs([populationFile,attritionFile,retirementFile],["population","attrition","retirement"],r)
                        resp = make_response({"succes":"succes"})
                        resp.set_cookie('globalID', globalID,max_age=100000000,samesite='Lax')
                        return resp
                else:
                    flash('Internal Error')
                    abort(500,message="Internal server error") 

    class LoadFiles(Resource): 
        def get(self):
            """
            get cookie
            ---
            tags:
                - File upload
            responses:
                200:
                    description: 
            """ 
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                resp = make_response({"result":readCSV(globalID,r)})
                return resp
            else:
                abort(400,"Couldn't find ID")

    class Supply(Resource):
        def get(self):
            """

            """
            if "globalID" in request.cookies:
                globalID = request.cookies.get("globalID")
                csvs = readCSV(globalID,r)
                supply = calculateSupply(csvs)
                resp = make_response({"result":"result"})
                return resp
            else:
                abort(400,"Couldn't find ID")
    
    # API resource routing
    api.add_resource(UploadFile, "/api/upload/")
    api.add_resource(LoadFiles, "/api/load/")
    api.add_resource(Supply, "/api/supply/")
 
    return app