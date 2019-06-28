import logging
from logging.handlers import TimedRotatingFileHandler

from d_growth.extentions import db, app
from d_growth.models import User
from d_growth.api import api_blueprint


def register_extensions(app):
    with app.app_context():
        db.init_app(app)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all(app=app)
        # update_db()

    @app.teardown_appcontext
    def shutdown_session(response_or_exc):
        db.session.remove()


def register_blueprints(app):
    app.register_blueprint(api_blueprint)


def configure_logs(app):
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    handler = TimedRotatingFileHandler('error.log', when='midnight', interval=1, backupCount=12)
    handler.suffix = "%Y_%m_%d" + ".log"
    logger.addHandler(handler)


def create_app(config):
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)
    return app
