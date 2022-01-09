import os

from flask import Flask
from flask import (redirect,url_for)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ecommerce.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

  
   
    
    #imports database
    from . import db
    db.init_app(app)

    #import blueprint for auth
    from . import auth
    app.register_blueprint(auth.bp)

    #import blueprint for shop and redirect for site.com/home to site.com/
    from . import shop
    app.register_blueprint(shop.bp)
    app.add_url_rule('/', endpoint='home')
    return app

