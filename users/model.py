from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(45))
    password = Column(String(45))
    rol_id = Column(Integer,ForeignKey('rol.id'))

    rol = relationship('Rol', backref='roles')

    def __repr__(self):
        return "<Users(email='{}', rol='{}')>".format(self.email, self.rol.rol)


class Rol(db.Model):
    __tablename__ = "rol"
    id = Column(Integer, primary_key=True)
    rol = Column(String(45))

    def __repr__(self):
        return "<Roles(id='{}', rol='{}')>".format(self.id, self.rol)


if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine

    db_name = 'cisyg.sqlite'
    if os.path.exists(db_name):
        os.remove(db_name)

    engine = create_engine("mysql://flask:123456@localhost/flask_cisyg")

    
    #Rol:
    # session.add(Rol(rol="Admin"))
    # session.add(Rol(rol="Vendedor"))
    # session.add(Rol(rol="Cajero"))
    # session.add(Rol(rol="Repositor"))
    # session.commit()

    #Users:
    # session.add(Users(email="jorge@example.com", password="123456", rol_id=1))# 1
    # session.add(Users(email="juan@example.com", password="123456", rol_id=2))# 1
    # session.add(Users(email="pepe@example.com", password="123456", rol_id=3))# 1
    # session.add(Users(email="jose@example.com", password="123456", rol_id=4))# 1

    # session.commit()
    # print("")
    # for u in session.query(Users).all():
        # print("")
        # print(u)
        # print("El usuario " + u.email + " tiene el rol "+ u.rol.rol)
    
    # print("")
    # print("")

    # for r in session.query(Rol).all():
        # print(r)


