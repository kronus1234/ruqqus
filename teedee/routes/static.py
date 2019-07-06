from teedee.helpers.wrappers import *
from flask import *
from teedee.__main__ import app

#take care of static pages

@app.route("/", methods=["GET"])
@auth_desired
def home(v)
    return render_template("home.html", v=v)

@app.route('/static/<path:path>')
def static_service(path):
    return send_from_directory('./static', path)

@app.route("/robots.txt", methods=["GET"])
def robots_txt():
    return send_from_directory("./static", "robots.txt")

@app.route("/settings", methods=["GET"])
@auth_required
def settings(v):
    return render_template("settings.html", v=v)
