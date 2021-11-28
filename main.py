from flask import Flask
from application.database import db

def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.sqlite3"
    app.config["DEBUG"]=False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
    db.init_app(app)
    return app

app=create_app()
app.app_context().push()


from application.models import *

from application.controllers import *

from application.api import *




if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080")