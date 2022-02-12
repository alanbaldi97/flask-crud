from utils.validate_errors import required
from pydantic import BaseModel

class UserValidator(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True
        error_msg_templates = {
          **required
        }

