from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# Ambil helper get_blueprints() dari views.py
from .views import get_blueprints


class IpbDataverseThemePlugin(plugins.SingletonPlugin):
    """IPB Dataverse theme plugin."""

    # Ubah konfigurasi (templates, static, dll)
    plugins.implements(plugins.IConfigurer)

    # Daftarkan Flask Blueprint
    plugins.implements(plugins.IBlueprint)

    def update_config(self, config: CKANConfig):
        # Template directory milik extension
        toolkit.add_template_directory(config, "templates")

        # Static/public files (CSS, gambar, dll)
        toolkit.add_public_directory(config, "public")
        # Kalau nanti perlu webassets:
        toolkit.add_resource("public", "ipb_dataverse_theme")

    def get_blueprint(self):
        """
        CKAN akan memanggil method (get_blueprint),
        bukan get_blueprints. Memanggil
        helper get_blueprints() dari views.py.
        Boleh return satu Blueprint atau list of Blueprint.
        """
        return get_blueprints()
