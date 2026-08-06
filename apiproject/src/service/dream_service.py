from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Dream
from src.repository.dream_repository import DreamRepository

class DreamService:
    def __init__(self, session):
        self.dream_repo = DreamRepository(session)
        self.session = session

    async def save(self, dream: Dream):
        return await self.dream_repo.save(dream)

    async def get_all_dreams(self):
        return await self.dream_repo.get_all_dreams()

    async def get_dream_by_id(self, id: int):
        dream = await self.dream_repo.get_dream_by_id(id)
        if not dream:
            raise ResourceNotFoundException(f"Resource with {id} not found")
        # await self.dream_repo.delete_dream(dream)
        return dream

    async def delete_dream(self, id: int):
        dream = await self.dream_repo.get_dream_by_id(id)
        if not dream:
            raise ResourceNotFoundException(f"Resource with {id} not found")
        await self.dream_repo.delete_dream(dream)
        return dream

    async def update_dream(self, dream: Dream):
        db_dream = await self.dream_repo.get_dream_by_id(dream.id)
        if not db_dream:
            raise ResourceNotFoundException(f"Resource with {dream.id} not found")
        db_dream.title = dream.title
        db_dream.description = dream.description
        db_dream.mood = dream.mood
        return db_dream
