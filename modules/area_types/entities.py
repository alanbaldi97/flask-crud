from database import db

class AreaType(db.Model):
    __tablename__ = "area_types"
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column(db.String(100))

