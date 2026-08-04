from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Post
from src.repository.post_repository import PostRepository

class PostService:
    def __init__(self, session):
        self.post_repo = PostRepository(session)

    async def create_post(self, post: Post):
        return await self.post_repo.create_post(post)

    async def fetch_all_post(self):
        return await self.post_repo.fetch_all_post()

    async def fetch_post_by_id(self, post_id: int):
        post = await self.post_repo.fetch_post_by_id(post_id)
        if not post:
            raise ResourceNotFoundException("Post not found")
        return post

    async def update_post(self, post_id:int, title:str=None, content:str=None):
        post = await self.post_repo.update_post(post_id, title, content)
        if not post:
            raise ResourceNotFoundException("Post not found")
        return post

    async def delete_post(self, post_id: int):
        post = await self.post_repo.delete_post(post_id)
        if not post:
            raise ResourceNotFoundException("Post not found")
        return post