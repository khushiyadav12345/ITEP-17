from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import User
from src.repository.user_repository import UserRepository

class UserService:
    def __init__(self, session):
        self.user_repo = UserRepository(session)

    async def create_user(self, user: User):
        return await self.user_repo.create_user(user)

    async def fetch_all_users(self):
        return await self.user_repo.fetch_all_users()

    async def fetch_user_by_id(self,user_id:int):
        user = await self.user_repo.fetch_user_by_id(user_id)
        if not user:
            raise ResourceNotFoundException("User not found")
        return user

    async def update_user(self,user_id:int, name: str=None, email:str=None, password:str=None):
        user = await self.user_repo.update_user(user_id, name, email, password)
        if not user:
            raise ResourceNotFoundException("User not found")
        return user

    async def delete_user(self, user_id: int):
        user = await self.user_repo.delete_user(user_id)
        if not user:
            raise ResourceNotFoundException("User not found")
        return user