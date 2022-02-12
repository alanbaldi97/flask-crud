import enum
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
from database import db
from modules.area_types.entities import AreaType

class Status(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'


class Manager(db.Model):
    __tablename__ = "managers"
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    area_type_id = db.Column(db.Integer, db.ForeignKey('area_types.id'))
    status = db.Column('status',Enum(Status))
    area_type = relationship(AreaType, backref='managers' ,uselist=False)

    def __init__(self, id = None, name = None, last_name = None, area_type_id = None, status = None ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.last_name = last_name
        self.area_type_id = area_type_id
        self.status = status

    def save(self):
        if self.id is None:
            db.session().add(self)
        else:
            db.session.merge(self)

        db.session().flush()
        db.session().commit()
    
    def delete(self):
        record = self.query.get(self.id)
        db.session().delete(record)
        db.session().commit() 
        


        

    

