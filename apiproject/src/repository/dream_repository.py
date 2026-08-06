from sqlalchemy import select

from src.model import Dream

class DreamRepository:
    def __init__(self, session):
        self.session = session

    async def save(self, dream: Dream):
        self.session.add(dream)
        return dream

    async def get_all_dreams(self):
        statement = select(Dream).order_by(Dream.id.desc())
        dream_list = await self.session.execute(statement)
        return dream_list.scalars().all()

    async def get_dream_by_id(self, id: int):
        return await self.session.get(Dream, id)

    async def delete_dream(self, dream: Dream):
        return await self.session.delete(dream)
