from flask import Blueprint, render_template, current_app
from domain.models.database import EEVEE_DB

home_views = Blueprint("home_views", __name__)

eevee_db = EEVEE_DB()


@home_views.route("/")
def home():
    return render_template(
        "home.html", master_set=current_app.master_set, grailed_data=[1]
    )
