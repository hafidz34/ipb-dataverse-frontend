import ckan.plugins.toolkit as tk


def ipb_dataverse_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "ipb_dataverse_theme_required": ipb_dataverse_theme_required,
    }
