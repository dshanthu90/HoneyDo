import os
from flask import Flask


def create_app(test_config=None):
    #Create and instantiate the app
    app=Flask(__name__, instance_relative_config=True)
    if test_config==None :
        app.config.from_pyfile('config.py', silent=True )
    else :
        app.config.from_pyfile('test_config.py',silent=True )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # A simple web page to instantiate the app
    @app.route('/')
    def page():
        return "Honey Do!"

    from HoneyDo import db
    db.init_app(app)
    return app


