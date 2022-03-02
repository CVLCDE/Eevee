from flask import Blueprint, render_template, current_app
from ..models.grailed_cards_model import GrailedCardsModel

home_route = Blueprint("home_route", __name__)

grailed_model = GrailedCardsModel()


@home_route.route("/")
def home():
    print("LOOK HERE")
    t = grailed_model.get_all_cards()
    print(t[0]["prices"])
    return render_template(
        "home.html",
        master_set=current_app.master_set,
        grailed_data=grailed_model.get_all_cards(),
    )
