from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True
app.config['EXPLAIN_TEMPLATE_LOADING '] = True
app.config['DEBUG'] = True

###### DATABASE: ###### 
# "mysql://<database_user>:<user_password>@<host>/<database>"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://flask:123456@localhost/flask_cisyg"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

from users.model import db
db.init_app(app)
# with app.app_context():
    # db.create_all()

###### MIGRATE: ###### 
from flask_migrate import Migrate

migrate = Migrate(app,db)
"""
Para crear las migraciones:
    flask db init (primera vez)
    luego:
        flask db migrate -m 'mensaje para migracion'
        flask db upgrade
"""


###### BLUEPRINTS: ###### 
from home.routes import home_mod
from users.routes import user_mod

app.register_blueprint(home_mod)
app.register_blueprint(user_mod)

if __name__ == '__main__':
    from users.model import Users
    u = Users()
    u.password = 'cat'
    print(u.password)
    print(u.password_hash)
    print(u.verify_password('dog'))
    print(u.verify_password('cat'))
    # app.run()
