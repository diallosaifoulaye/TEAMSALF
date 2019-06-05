from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import dash
import dash_core_components 
import dash_html_components
import matplotlib.pyplot




app = Flask(__name__)
##################################"Configuration"
app.config['SECRET_KEY'] = '6b723afcf7c57be1d0c3cda1ad7e8a9a'       
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
das = dash.Dash()

login_manager.login_view = 'login'
from appli import routes