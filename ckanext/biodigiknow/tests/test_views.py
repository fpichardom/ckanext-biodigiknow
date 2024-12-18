"""Tests for views.py."""

import pytest

import ckanext.biodigiknow.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "biodigiknow")
@pytest.mark.usefixtures("with_plugins")
def test_biodigiknow_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("biodigiknow.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, biodigiknow!"
