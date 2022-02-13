from database import db
from flask_bcrypt import check_password_hash
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)


    def check_password(self,password):
        return check_password_hash(self.password, password)


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, jti = None, created_at = None) -> None:
        super().__init__()

        self.jti = jti
        self.created_at = created_at
    
    def save(self):
        db.session().add(self)
        db.session().commit()

    
    def select(*params):
        return db.session().query(*params)

