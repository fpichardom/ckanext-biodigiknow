"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.biodigiknow.logic import validators


def test_biodigiknow_reauired_with_valid_value():
    assert validators.biodigiknow_required("value") == "value"


def test_biodigiknow_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.biodigiknow_required(None)
