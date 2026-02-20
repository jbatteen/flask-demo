from flask import Flask, render_template, request, redirect, jsonify, make_response, url_for, g
import os

this_files_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_files_dir)
app = Flask(__name__)

@app.before_request
def before_request_function():
    # this stuff happens before your routes and can be used to load stuff into g or whatever else you want to do
    pass

@app.after_request
def after_request_function(response):
    # this stuff happens after your routes and can be used for all sorts of stuff
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    match request.method:
        case 'POST':
            flask_data = request.form.get('flask_data')
            if flask_data is None:
                return jsonify({'success': False, 'error': 'Must include flask_data in form'})
            print(flask_data)
            return jsonify({'success': True})
        case _:
            return render_template('index.html.j2')
