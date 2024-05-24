from spyne import ComplexModel, Unicode
from dataclasses import dataclass

@dataclass
class UserSchema(ComplexModel):
    id: str = Unicode(80, pk=True)
    name: str = Unicode(150, min_len=4, pattern='[a-z0-9.]+')
    email: str = Unicode(150)
    address: str = Unicode(250)
    date_of_birth: str = Unicode(250)

    def __init__(self, id: str, name: str, email: str, address: str, date_of_birth: str):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.date_of_birth = date_of_birth