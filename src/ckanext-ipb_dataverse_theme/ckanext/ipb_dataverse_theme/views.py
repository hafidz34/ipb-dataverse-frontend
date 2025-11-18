from flask import Blueprint, render_template

# Blueprint utama untuk tema IPB Dataverse
ipb_dataverse_theme = Blueprint(
    "ipb_dataverse_theme",
    __name__,
)

# Halaman bantuan: http://localhost:5000/help
@ipb_dataverse_theme.route("/help")
def help_page():
    # Pakai template: templates/home/help.html
    return render_template("home/help.html")


# Route test lama untuk memastikan Blueprint terdaftar
def page():
    return "Hello, ipb_dataverse_theme!"


# Endpoint lama untuk test Blueprint
ipb_dataverse_theme.add_url_rule(
    "/ipb_dataverse_theme/page",
    view_func=page,
)


def get_blueprints():
    """Dikembalikan ke CKAN lewat plugin.get_blueprints()."""
    return [ipb_dataverse_theme]
