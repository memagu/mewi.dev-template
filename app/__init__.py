from flask import Flask

from .config import CONFIGURATIONS
from .views.home import home


def create_app(configuration: str = "production") -> Flask:
    app = Flask(__name__)
    app.config.from_object(CONFIGURATIONS[configuration])

    app.register_blueprint(home, url_prefix="")

    return app
