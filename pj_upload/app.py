from flask import Flask
from mi import key
from flask_debug import Debug

UPLOAD_FOLDER = '~/upload'

app = Flask(__name__)
app.secret_key = key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
