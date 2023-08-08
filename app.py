import os
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
from functools import wraps
from cs50 import SQL
import base64

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///database.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            flash("Please add username")
        elif not request.form.get("password"):
            return render_template('error.html')
        elif not request.form.get("confirmation"):
            return render_template('error.html')
        elif request.form.get("password") != request.form.get("confirmation"):
            return render_template('error.html')

        check = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(check) != 0:
            return render_template('error.html')

        db.execute("INSERT INTO users (username, hash, first_name, last_name) VALUES (?, ?, ?, ?)", request.form.get("username"), generate_password_hash(request.form.get("confirmation")), request.form.get("first_name"), request.form.get("last_name"))

        check = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        
        flash("Account successfully created")

        return render_template('index.html')
    
       

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template('error.html')
        elif not request.form.get("password"):
            return render_template('error.html')

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template('error.html')

        session["user_id"] = rows[0]["id"]

        return redirect('/home')


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/post", methods=["GET", "POST"])
@login_required
def post():
    if request.method == "POST":
        user_id = session["user_id"]
        file = request.files["file"]
        image = base64.b64encode(file.read())
        title = request.form.get("title")
        text = request.form.get("text")

        
        if not text:
            return render_template('error.html')

        db.execute("INSERT INTO posts (user_id, image, title, text) VALUES (?, ?, ?, ?)", user_id, image, title, text)
        
        return redirect("/home")

    else:
        posts = db.execute("SELECT * FROM posts ORDER BY timestamp DESC")
        image = db.execute("SELECT image FROM posts ORDER BY timestamp DESC")
        id = session["user_id"]
        if id == 1:
            return render_template("post.html", posts=posts, image=image)
        else:
            return render_template('forbidden.html')


@app.route("/home", methods=["GET"])
@login_required
def home():
        posts = db.execute("SELECT * FROM posts ORDER BY timestamp DESC")
        image = db.execute("SELECT image FROM posts ORDER BY timestamp DESC")
        return render_template("home.html", posts=posts, image=image)
        

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM posts WHERE id = ?", id)
    return redirect("/post")


if __name__ == "__main__":
    app.run(debug=True)