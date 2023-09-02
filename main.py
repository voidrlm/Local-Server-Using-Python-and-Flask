from flask import Flask, jsonify

from db.users import data_list

app = Flask(__name__)

print("Local Server running...")


@app.route("/get_data", methods=["GET"])
def get_data():
    try:
        return jsonify(data_list)
    except:
        # Handle the exception
        print("error")


if __name__ == "__main__":
    app.run(debug=True),
