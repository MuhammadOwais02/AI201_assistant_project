from flask import Flask

def creak_app():
    app = Flask(__name__)
    app.config['key'] = 'a string'

    #blueprints registered here
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app

    