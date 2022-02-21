import base64
import json
import requests
from hashlib import sha1
from flask import Flask, request, jsonify
 
app = Flask(__name__)


@app.route('/save', methods=['POST'])
def post_something():
    param = request.form.get('data')
    print(param)
    #f=json.loads(param)
    #print(f)
    #d={}
    with open("accounts.json", "a") as f:
        f.write(f"{param},")
        print("Saved in File accounts.json")
    return param


@app.route('/')
def index():
    return "<h1>Bakugo</h1>"


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
