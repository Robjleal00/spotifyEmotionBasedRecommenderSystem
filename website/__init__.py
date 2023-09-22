from flask import Flask 
import os

def create_app():
    app = Flask(__name__)
    website_secret_key = os.getenv("WEBSITE_SECRET_KEY")
    app.config["SECRET_KEY"] = website_secret_key

    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app