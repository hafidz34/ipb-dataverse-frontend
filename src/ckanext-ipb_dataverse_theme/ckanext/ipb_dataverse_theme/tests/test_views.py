"""Tests for views.py."""

import pytest

import ckanext.ipb_dataverse_theme.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "ipb_dataverse_theme")
@pytest.mark.usefixtures("with_plugins")
def test_ipb_dataverse_theme_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("ipb_dataverse_theme.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, ipb_dataverse_theme!"
