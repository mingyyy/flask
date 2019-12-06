#!../venv/bin/python
from flask import Flask, jsonify
from helper import URL

app = Flask(__name__)


@app.route('/tinyuri/api/v1.0/<string:long_url>', methods=['PUT', 'POST'])
def shorten_uri(long_url):
    short_url = URL()
    print("Fine from here")
    return jsonify({'short_url': short_url.get_short(long_url)})


@app.route('/tinyuri/api/v1.0/<string:short_url>', methods=['GET'])
def get_long_uri(short_url):
    long_url = URL()
    return jsonify({'long_url': long_url.get_long(short_url)})


@app.route('/tinyuri/api/v1.0/<string:url>', methods=['DELETE'])
def delete_uri(url):
    remove_url = URL()
    return remove_url.delete_record(url)


if __name__ == '__main__':
    app.run(debug=True)
