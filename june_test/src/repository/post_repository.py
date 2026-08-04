from sqlalchemy import select
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Post

class PostRepository:
    def __init__(self,session):
        self.session = session

    async def create_post(self,post:Post):
        self.session.add(post)
        await self.session.flush()
        return post

    async def fetch_all_post(self):
        statement = select(Post)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def fetch_post_by_id(self,post_id:int):
        return await self.session.get(Post,post_id)

    async def update_post(self,post_id:int,title:str,content:str):
        post = await self.session.get(Post,post_id)
        post.title = title
        post.content = content
        await self.session.flush()
        return post

    async def delete_post(self,post_id:int):
        post = await self.session.get(Post,post_id)
        await self.session.delete(post)
        await self.session.flush()
        return post