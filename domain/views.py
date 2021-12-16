from flask import Blueprint, render_template
from pokemontcgsdk import Set

views = Blueprint("views", __name__)


def get_all_sets():
    return Set.all()


def get_all_set_names():
    sets = get_all_sets()
    set_names = [tcg_set.name for tcg_set in sets][::-1]
    return set_names


def get_all_set_logos():
    sets = get_all_sets()
    set_logos = [tcg_set.images.logo for tcg_set in sets][::-1]
    return set_logos


def get_all_set_totals():
    sets = get_all_sets()
    set_totals = [tcg_set.total for tcg_set in sets][::-1]
    return set_totals


@views.route("/")
def home():
    set_names = get_all_set_names()
    set_logos = get_all_set_logos()
    set_totals = get_all_set_totals()
    return render_template(
        "home.html", set_names=set_names, set_logos=set_logos, set_totals=set_totals
    )


@views.route("/grailed")
def grailed_list():
    return render_template("grailed.html")


@views.route("/sets")
def set_list():
    set_names = get_all_set_names()
    set_logos = get_all_set_logos()
    set_totals = get_all_set_totals()
    return render_template(
        "sets.html",
        set_names=set_names,
        set_logos=set_logos,
        set_totals=set_totals,
    )


@views.route("/sets/<string:id>")
def set_page():
    return render_template("set_page.html")
