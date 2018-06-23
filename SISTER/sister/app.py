from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash
import requests
import json

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('home.html')

@app.route('/create',methods=['POST'])
def create():
    if request.method == 'POST':
        return "yesss"



if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port=5028)
