from flask import Flask, make_response, jsonify, flash
from flask_restful import Api, Resource, reqparse, request, abort
from werkzeug.utils import secure_filename
import werkzeug
import os
#For documentation
from flasgger import Swagger, swag_from
#Database
import redis
#Our files
from FileHandling import writeCSV


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
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SWAGGER'] = {
        'title': 'My API',
        'uiversion': 3,
        "specs_route": "/swagger/"
        }
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
                    description: 
                401:
                    description: One of the files is empty meaning no file was sent in
                402:
                    description: One of the files isn't a csv
                200:
                    description: succes returns a json with the csv
            """
            # check if the post request has the file part
            parse = reqparse.RequestParser()
            parse.add_argument('file', type= werkzeug.datastructures.FileStorage, location='files')
            args = parse.parse_args()

            abort(400,message="Population is missing got " + str(args))
            if 'Population.csv' not in request.files:
                flash('Population is missing')
                abort(400,message="Population is missing got " + str(request.files.values()))
            elif 'Attrition.csv' not in request.files:
                flash('Attrition is missing')
                abort(401,message="Attrition is missing" + str(request.files))
            elif 'Retirement.csv' not in request.files:
                flash('Retirment is missing')
                abort(402,message="Retirement is missing" + str(request.files))
            else:
                populationFile = request.files['Population.csv']
                attritionFile = request.files['Attrition.csv']
                retirementFile = request.files['Retirement.csv'] 
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
                if populationFile.filename == '':
                    flash('No Population file selected')
                    abort(410)
                elif attritionFile.filename == '':
                    flash('No Attrition file selected')
                    abort(411)
                elif retirementFile.filename == '':
                    flash('No Retirement file selected')
                    abort(412)
                elif populationFile and attritionFile and retirementFile and map(lambda x: allowed_file(x,{'csv'}),[populationFile,attritionFile,retirementFile]):
                    if not(allowed_file(populationFile.filename,{'csv'})):
                        flash('Population is not a csv')
                        abort(420)
                    elif not(allowed_file(attritionFile.filename,{'csv'})):
                        flash('Attrition is not a csv')
                        abort(421)
                    elif not(allowed_file(retirementFile.filename,{'csv'})):
                        flash('Retirement is not a csv')
                        abort(422)
                    else: 
                        result = writeCSV([populationFile,attritionFile,retirementFile],["Population","Attrition","Retirement"],r)
                        return {"result" : result}, 200
                else:
                    flash('Internal Error')
                    abort(500)

    class LoadFile(Resource):
        def PUT(self):
            

            return {}, 200

    # API resource routing
    api.add_resource(UploadFile, "/API/upload/")
        
    return app