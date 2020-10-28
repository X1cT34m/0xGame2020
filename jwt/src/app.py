from flask import Flask, request, render_template, make_response, redirect, Request, url_for
from cookie import *
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['user']
        passwd = request.form['passwd']
    payload = {
        "user": user,
        "passwd": passwd,
        "uid": str(uuid.uuid4()),
        "role": "guest"
    }
    response = make_response(redirect(url_for("flag")))
    response.set_cookie("JWT", generate_jwt(payload, "njupt"), max_age=1800)
    return response

@app.route("/flag")
def flag():
    res = verify_jwt(request.cookies.get("JWT"), "njupt")
    if res['user'] == "admin" and res['role'] == "admin":
        return render_template("res.html", title="Congratulations", content="0xGame{JWT_is_th3_f14g}")
    else:
        tips = "Welcome "+res['user']+" ,but you are not admin!"
        return render_template("res.html", title="Permission denied", content=tips)

if __name__ == "__main__":
    app.run()
