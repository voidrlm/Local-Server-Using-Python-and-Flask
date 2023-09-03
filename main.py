from flask import Flask, jsonify, request

app = Flask(__name__)

from db.users import data


@app.route("/api/get_all", methods=["GET"])
@app.route("/api/add_item", methods=["POST"])
def handle_data():
    if request.method == 'GET':
        output = {'status': 'success', 'data': data}
        return jsonify(output)
    elif request.method == 'POST':
        new_item = request.json
        data.append(new_item)
        output = {'status': 'success'}
        return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
