from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import *
from .controllers import *
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def index():
    return {'message': 'Pizza API is running!'}, 200
