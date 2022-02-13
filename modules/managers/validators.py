import enum
from typing import Optional
from pydantic import BaseModel
from modules.area_types.validators import AreaTypeValidator
from utils.validate_errors import required

class TypeStatus(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class ManagerValidator(BaseModel):
    id: Optional[int]
    img: str = None
    name: str
    last_name: str
    email: str
    area_type_id: int
    status: TypeStatus = TypeStatus.Activo
    area_type: Optional[AreaTypeValidator]
    class Config:
        orm_mode = True
        error_msg_templates = {**required}

    
