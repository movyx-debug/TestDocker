from flask import Flask

def create_app(db_url=None):
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
