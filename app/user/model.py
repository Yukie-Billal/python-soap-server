from app.core.db import BaseModel
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Date, Integer, Numeric

class UsersModels(BaseModel):

    __tablename__ = "users"

    id: str = Column(String(255), primary_key=True, default=lambda: uuid4())
    name: str = Column(String(250))
    email: str = Column(String(250))
    password: str = Column(String(250))
    date_of_birth: Date = Column(Date, default=lambda: datetime.now())
    address: str = Column(String(250))

    def __init__(self, name, email, hashed_password, date_of_birth, address):
        self.name = name
        self.email = email
        self.password = hashed_password
        self.date_of_birth = date_of_birth
        self.address = address

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'date_of_birth': str(self.date_of_birth),
            'address': self.address,
        }