from flask import Blueprint, render_template, current_app
from domain.tools import ptcg_sdk

grailed_views = Blueprint("grailed_views", __name__)

@grailed_views.route("/grailed")
def all_grails():
    return render_template("grailed.html")