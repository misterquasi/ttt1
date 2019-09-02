from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("tem1.html", varpassed="Called from the index")


@app.route("/alt")
def alt():
    return render_template("tem1.html", varpassed="Called from alt")

@app.route("/templated")
def templated():
    #return render_template("base.html")
    return render_template("basecall.html")


