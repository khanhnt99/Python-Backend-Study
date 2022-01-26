from crypt import methods
from curses import flash
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Khanh"}
    posts = [
        {"author": {"username": "Nguyen"}, "body": "Flask de hoc qua phai khong"},
        {"author": {"username": "Tran"}, "body": "Lap trinh Web that thu vi"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Yeu cau dang nhap tu User {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect('/index')
    return render_template("login.html", title="Sign In", form=form)
