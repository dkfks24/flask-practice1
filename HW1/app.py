from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_template_render():
    return render_template("main.html")

@app.route("/profile")
def profile_template_render():
    hobbies = ['산책', '카페가기', 'ott시청']
    return render_template("profile.html", hobbies=hobbies)

@app.route("/greet/<name>")
def greet_name(name):
    return render_template("greet.html", name=name)