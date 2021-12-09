from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/grailed")
def grailed_list():
    return render_template("grailed_list.html")


@views.route("/sets")
def set_list():
    return render_template("set_list.html")


@views.route("/sets/<string:id>")
def set_page():
    return render_template("set_page.html")
