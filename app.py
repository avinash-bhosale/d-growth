# - coding: utf-8 --
from os import environ
from sys import exit

from flask_migrate import Migrate
from flask_cors import CORS
from d_growth import create_app, db
from config import config_dict

get_config_mode = environ.get('AGILE_CONFIG_MODE', 'Development')  # Production
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid AGILE_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
app.app_context().push()
Migrate(app, db)
cors = CORS(app, resources={r"/*": {"origins": "*"}})