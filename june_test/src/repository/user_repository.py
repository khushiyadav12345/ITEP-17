from sqlalchemy import select
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import User

class UserRepository:
    def __init__(self, session):
        self.session = session

    async def create_user(self,user:User):
        self.session.add(user)
        await self.session.flush()
        return user

    async def fetch_all_users(self):
        statement = select(User)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def fetch_user_by_id(self,user_id:int):
        return await self.session.get(User,user_id)

    async def update_user(self,user_id:int, name:str=None, email:str=None, password:str=None):
        user = await self.session.get(User,user_id)
        if not user:
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password

        await self.session.flush()
        return user

    async def delete_user(self,user_id:int):
        user = await self.session.get(User, user_id)
        if not user:
            return None

        await self.session.delete(user)
        await self.session.flush()
        return user