from flask import Flask

from .config import CONFIGURATIONS
from .views.home import home
from .views.about import about
from .views.contact import contact


def create_app(configuration: str = "production") -> Flask:
    app = Flask(__name__)
    app.config.from_object(CONFIGURATIONS[configuration])

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(about, url_prefix="/about/")
    app.register_blueprint(contact, url_prefix="/contact/")

    return app
