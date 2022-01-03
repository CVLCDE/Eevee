from flask import Blueprint, render_template, current_app
from domain.tools import ptcg_sdk

set_views = Blueprint("set_views", __name__)


@set_views.route("/all_sets")
def all_sets():
    return render_template("all_sets.html", set_id=current_app.master_set)


@set_views.route("/all_sets/<string:id>")
def specific_set(id):
    set_data = current_app.master_set[id]
    set_cards = set_data["set_cards"](id)
    return render_template("specific_set.html", set_data = set_data, set_cards = set_cards)
