"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.ipb_dataverse_theme.logic import validators


def test_ipb_dataverse_theme_reauired_with_valid_value():
    assert validators.ipb_dataverse_theme_required("value") == "value"


def test_ipb_dataverse_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.ipb_dataverse_theme_required(None)
