from flask import Flask
from flask import render_template
from flask import request
from server.build_chatbot import build_chatbot 
import json 

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/", methods=["POST", "GET"])
def joined():
    if request.method == "POST":
        print("success")
        name = request.form['name']
        print(1)
        age = request.form['age']
        print(2)
        gender = request.form['gender']
        print(3)
        country = request.form['country']
        print(4)
        interest_1 = request.form['interest1']
        print(5)
        interest_2 = request.form['interest2']
        print(6)
        interest_3 = request.form['interest3']
        print("got all requests")
        prompt = build_chatbot(name,age,gender,country,interest_1,interest_2, interest_3)
        return render_template('response.html', prompt=prompt)

    return render_template('index.html')




