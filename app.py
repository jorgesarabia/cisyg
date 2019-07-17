from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True
app.config['EXPLAIN_TEMPLATE_LOADING '] = True
app.config['DEBUG'] = True

# app.config.from_pyfile('config.py')

from home.routes import home_mod
from users.routes import user_mod

app.register_blueprint(home_mod)
app.register_blueprint(user_mod)

if __name__ == '__main__':
    app.run()
