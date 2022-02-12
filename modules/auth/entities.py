from database import db
from flask_bcrypt import check_password_hash
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)


    def check_password(self,password):
        return check_password_hash(self.password, password)
