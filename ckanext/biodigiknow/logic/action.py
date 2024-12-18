import ckan.plugins.toolkit as tk
import ckanext.biodigiknow.logic.schema as schema


@tk.side_effect_free
def biodigiknow_get_sum(context, data_dict):
    tk.check_access(
        "biodigiknow_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.biodigiknow_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'biodigiknow_get_sum': biodigiknow_get_sum,
    }
