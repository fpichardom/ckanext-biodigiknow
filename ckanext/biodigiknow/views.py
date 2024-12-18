from flask import Blueprint


biodigiknow = Blueprint(
    "biodigiknow", __name__)


def page():
    return "Hello, biodigiknow!"


biodigiknow.add_url_rule(
    "/biodigiknow/page", view_func=page)


def get_blueprints():
    return [biodigiknow]
