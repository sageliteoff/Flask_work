from flask import Flask, render_template, redirect
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
    searchfrom = SearchBarForm()
    if searchfrom.validate_on_submit():
        return render_template("citysearch.html", form = searchfrom)
    return render_template("citysearch.html", form=searchfrom)
