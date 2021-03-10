from flask import Flask, request, jsonify
app = Flask(__name__)

global all_msg
all_msg = dict()

@app.route('/logger', methods=['GET', 'POST'])
def logger_f():
    global all_msg
    if request.method == 'POST':
        input_json = request.get_json(force=True)
        all_msg[input_json["uuid"]] = input_json['msg']
        print("Adding key: {}, msg: {}".format(input_json["uuid"], input_json["msg"]))
        return jsonify({"is_success": True})
    
    if request.method == 'GET':
        return jsonify(all_msg)

if __name__ == "__main__":
    app.run(port=5001)