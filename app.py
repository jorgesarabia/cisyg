from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.py')

from home.routes import home_mod

app.register_blueprint(home_mod)

if __name__ == '__main__':
    app.run()
