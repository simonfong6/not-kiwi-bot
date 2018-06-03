#!/env/usr/bin python
"""
server.py

Tool to visualize GPS coordinates for donkeycar.
"""

from flask import Flask, request, send_from_directory, jsonify
import json

# File that stores the GPS markers
DATA_FILE = 'data.json'

# JSON status messages
SUCCESS = {'status' : {'success': True}}
FAIL = {'status': {'success': False}}

app = Flask(__name__)


@app.route('/')
def index():
    """ Serve the index page.
    """
    return send_from_directory('.', 'index.html')

@app.route('/markers')
def get_markers():
    """ Reads from the data file and returns the markers as JSON.
    """
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    
    return jsonify(data)
    
@app.route('/markers/replace', methods=['GET','POST'])
def replace_markers():
    """ Replaces all markers in the data file with the ones given.
    """
    markers = request.json
    data = {'markers': markers}

    with open(DATA_FILE, 'r+') as f:

        f.seek(0)
        
        json.dump(data, f, indent=4)
        
        f.truncate()
        
    return jsonify(SUCCESS)
    
@app.route('/markers/add', methods=['GET','POST'])
def add_markers():
    """ Appends a given marker to the data file.
    """
    
    marker = request.json['marker']    

    with open(DATA_FILE, 'r+') as f:
        
        data = json.load(f)
        data['markers'].append(marker)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        
    return jsonify(SUCCESS)
	
if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=3148)
