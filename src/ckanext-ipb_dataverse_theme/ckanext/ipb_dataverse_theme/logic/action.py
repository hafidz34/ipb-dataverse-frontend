import ckan.plugins.toolkit as tk
import ckanext.ipb_dataverse_theme.logic.schema as schema


@tk.side_effect_free
def ipb_dataverse_theme_get_sum(context, data_dict):
    tk.check_access(
        "ipb_dataverse_theme_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.ipb_dataverse_theme_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'ipb_dataverse_theme_get_sum': ipb_dataverse_theme_get_sum,
    }
