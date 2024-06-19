from flask import Flask
from dotenv import load_dotenv
from model import db
from flask_migrate import Migrate
from auth.auth import auth_bp
from home.home import home_bp
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get('DATABASE_URL') #os.getenv('DATABASE_URL')
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'SCHRODINGER'

Migrate(app, db)
db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)

app.add_url_rule("/", endpoint='index')
if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=False, host="0.0.0.0", port=8080)