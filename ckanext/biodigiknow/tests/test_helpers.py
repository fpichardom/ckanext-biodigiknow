"""Tests for helpers.py."""

import ckanext.biodigiknow.helpers as helpers


def test_biodigiknow_hello():
    assert helpers.biodigiknow_hello() == "Hello, biodigiknow!"
