import copy
from flask import Flask, request, jsonify
import requests as rq
import json
app = Flask(__name__)

global unique_id
unique_id = 0

@app.route('/facade', methods=['GET', 'POST'])
def facade_f():
    if request.method == 'POST':
        global unique_id
        input_json = request.get_json(force=True)
        input_json["uuid"] = unique_id
        unique_id += 1
        output_json = copy.deepcopy(input_json)
        rq.post("http://localhost:5001/logger", json=output_json)
        return output_json
    
    if request.method == 'GET':
        results_logger = rq.get("http://localhost:5001/logger")
        results_logger = json.dumps(results_logger.json())
        results_message = rq.get("http://localhost:5002/message")
        return results_logger + "\n. Message service output:" + results_message.text

if __name__ == "__main__":
    app.run(port=5000)