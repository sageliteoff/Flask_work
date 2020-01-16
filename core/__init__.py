from flask import Flask, render_template, redirect
import requests as res
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "125xxd12"

from .forms import SignUpForm, SearchBarForm

@app.route("/", methods=["POST", "GET"])
def index():
    signupform = SignUpForm()
    return render_template("index.html", form = signupform)

@app.route("/show", methods=["POST", "GET"])
def show():
    signupform = SignUpForm()
    if signupform.validate_on_submit():
        return render_template("result.html", form = signupform)
    return render_template("result.html", form=signupform)


@app.route("/city", methods=["POST", "GET"])
def CityHome():
    form = SearchBarForm()
    print(form.searchbar)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        city = form.searchbar.data
        api_key = "2ebb6b44b2cd0f0931930e3f7d5d9d92"
        clean_data = res.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}").json()
        return render_template("citysearch.html", form = form, data = clean_data)
    return render_template("citysearch.html", form=form)
