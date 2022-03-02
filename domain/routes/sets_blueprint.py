from flask import Blueprint, render_template, request, current_app
from ..models.grailed_cards_model import GrailedCardsModel
from ..models.owned_cards_model import OwnedCardsModel

set_views = Blueprint("set_views", __name__)
grailed_model = GrailedCardsModel()
owned_model = OwnedCardsModel()


@set_views.route("/all_sets")
def all_sets():
    return render_template("all_sets.html", master_set=current_app.master_set)


@set_views.route("/all_sets/<string:id>")
def specific_set(id):
    grailed_data = [card_obj["card_id"] for card_obj in grailed_model.get_all_cards()]
    owned_data = [card_obj["card_id"] for card_obj in owned_model.get_all_cards()]
    return render_template(
        "specific_set.html",
        set_data=current_app.master_set[id],
        set_cards=current_app.master_set[id]["set_cards"](id),
        grailed_cards=grailed_data,
        owned_cards=owned_data,
    )


# ---------------------------------------------------------------------------------------------
@set_views.route("/update_db", methods=["POST"])
def update_db():
    card_id = request.form["card_id"]
    card_status = request.form["status"]

    if card_status == "owned":
        owned_model.add_card(card_id)
    elif card_status == "not-owned":
        owned_model.remove_card(card_id)
    elif card_status == "grailed":
        grailed_model.add_card(card_id)

    return "testing"
