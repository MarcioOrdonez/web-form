import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Setting SQLite database system path
project_dir = os.path.dirname(os.path.abspath(__file__))
sqlite_path = 'sqlite:///../database/database.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_path
app.config['SECRET_KEY'] = 'A_VeRy_SeCrEtY_KeY'

db = SQLAlchemy(app)


from .models import User
from .models import Schema
from .models import Answered

db.create_all(app=app)



if __name__ == '__main__':
    app.run()