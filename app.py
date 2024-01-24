from flask import Flask, request, jsonify
import fixmyjson


app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_json(impo):
    data = request.get_json()
    
    
    if data is None:
        return "Invalid JSON object", 400
    
    # Do something with the JSON object
    return impo

@app.route("/", methods=["POST"])
def handle_json_file():
    data = request.files["file"].read()
    
    if not isinstance(data, dict):
        return "Invalid JSON file", 400
    
    # Do something with the JSON file.

    
    return jsonify({"message": "JSON file processed successfully"}) 
