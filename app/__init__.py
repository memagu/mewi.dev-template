from flask import Flask

from .views.home import home


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(home, url_prefix="")

    return app


