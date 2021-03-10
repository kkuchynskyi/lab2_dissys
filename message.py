from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/message', methods=['GET'])
def message_f():
    
    if request.method == 'GET':
        return "Not implemented yet"

if __name__ == "__main__":
    app.run(port=5002)