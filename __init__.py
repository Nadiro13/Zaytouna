from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # de flask app
app.config['SECRET_KEY'] = 'fd3d2cbd4d8fafa22eafa6bf32b26797'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# dit is een beveiligingskey waar ik de werking beetje vn ben vergeten maar bassicly da runt de pagina ni
# als de gebruikers key ni de secretkey matcht, die key heb ik via python in terminal via een module gecreert
# kweni zeker ofda ook hash is fni though
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # gebruik ik om ww te hashen en te decrypte om te checken
login_manager = LoginManager(app)  # daddy's fav klasse of all time baby, zo vanzelfsprekend jeeezus i love it
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
