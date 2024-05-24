from spyne import rpc, Unicode, Array, ServiceBase

from app.user.model import UsersModels
from app.user.schema import UserSchema

from app.core.db import session_factory

class UsersService(ServiceBase):
    
    @rpc(Unicode, _returns=Array(UserSchema))
    def get_users(ctx, id):
        session = session_factory()
        users_query = session.query(UsersModels)
        session.close()
        
        users = users_query.all()
        return [UserSchema(**u.json()) for u in users]
    
    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=UserSchema)
    def create_user(xtc, name, email, password, date_of_birth, address):
        session = session_factory()

        user = UsersModels(name, email, password, date_of_birth, address)

        session.add(user)
        session.commit()
        return UserSchema(user.id, user.name, user.email, user.address, str(user.date_of_birth))