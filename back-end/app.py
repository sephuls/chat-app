from flask import Flask, send_from_directory, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['POST'])
def get_map_cutout_by_zipcode_post():
    response = request.get_json()

    return jsonify({'resp': response})


if __name__ == '__main__':
    app.run(debug=True)
