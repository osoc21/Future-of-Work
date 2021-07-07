import os
from flask import Flask, jsonify, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import pandas as pd

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @app.route("/api/hello", methods=["GET"])
    def sample_route():
        return jsonify({"message": "This is a sample route"})

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pathName = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(pathName)
                df = pd.read_csv(pathName)
                return jsonify({"message": str(df)})
                
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''

    return app
