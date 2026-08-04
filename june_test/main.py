import asyncio

from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal, engine
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import User
from src.model.post import Post
from src.service.user_service import UserService
from src.service.post_service import PostService

async def fetch_all_users():
    try:
        async with SessionLocal() as session:
            user_service = UserService(session)
            user_list = await user_service.fetch_all_users()
            for user in user_list:
                print(f"{user.id}:{user.name}:{user.email}")
    except SQLAlchemyError as e:
        print(e)

async def create_user():
    try:
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        password = input("Enter user password: ")
        async with SessionLocal.begin() as session:
            user = User(name=name, email=email, password=password)
            user_service = UserService(session)
            user = await user_service.create_user(user)
            await session.refresh(user)
            print(f"{user.id}:{user.name}:{user.email}")
    except SQLAlchemyError as e:
        print(e)

async def fetch_user_by_id():
    try:
        async with SessionLocal() as session:
            user_service = UserService(session)
            id = int(input("Enter user id: "))
            user = await user_service.fetch_user_by_id(id)
            print(f"{user.id}:{user.name}:{user.email}")
            print("Posts by this user:")
            if not user.posts:
                print("no post here")
            for post in user.posts:
                print(f"{post.id}:{post.title}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def update_user():
    try:
        async with SessionLocal.begin() as session:
            user_service = UserService(session)
            id = int(input("Enter user id: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            password = input("Enter new password: ")
            user = await user_service.update_user(id, name, email, password)
            print(f"{user.id}:{user.name}:{user.email}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def delete_user():
    try:
        async with SessionLocal.begin() as session:
            user_service = UserService(session)
            id = int(input("Enter user id: "))
            await user_service.delete_user(id)
            print("User deleted successfully")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def create_post():
    try:
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        user_id = int(input("Enter user id: "))
        async with SessionLocal.begin() as session:
            user_service = UserService(session)
            user = await user_service.fetch_user_by_id(user_id)
            post = Post(title=title, content=content, user_id=user_id)
            post_service = PostService(session)
            post = await post_service.create_post(post)
            await session.refresh(post)
            print(f"{post.id}:{post.title}:{post.content}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def fetch_all_post():
    try:
        async with SessionLocal() as session:
            post_service = PostService(session)
            post_list = await post_service.fetch_all_post()
            for post in post_list:
                print(f"{post.title}:{post.content}:{post.user.name}")
    except SQLAlchemyError as e:
        print(e)

async def fetch_post_by_id():
    try:
        async with SessionLocal() as session:
            post_service = PostService(session)
            id = int(input("Enter post id: "))
            post = await post_service.fetch_post_by_id(id)
            print(f"{post.id}:{post.title}:{post.content}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def update_post():
    try:
        async with SessionLocal.begin() as session:
            post_service = PostService(session)
            id = int(input("Enter post id: "))
            title = input("Enter new title: ")
            content = input("Enter new content: ")
            post = await post_service.update_post(id, title, content)
            print(f"{post.id}:{post.title}:{post.content}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def delete_post():
    try:
        async with SessionLocal.begin() as session:
            post_service = PostService(session)
            id = int(input("Enter post id: "))
            await post_service.delete_post(id)
            print("Post deleted successfully")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def main():
    while True:
        print("1 for creating user")
        print("2 for fetching all users")
        print("3 for fetching user by id")
        print("4 for updating user")
        print("5 for deleting user")
        print("6 for creating post")
        print("7 for fetching all posts")
        print("8 for fetching post by id")
        print("9 for updating post")
        print("10 for deleting post")
        print("0 for exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            await create_user()
        elif choice == 2:
            await fetch_all_users()
        elif choice == 3:
            await fetch_user_by_id()
        elif choice == 4:
            await update_user()
        elif choice == 5:
            await delete_user()
        elif choice == 6:
            await create_post()
        elif choice == 7:
            await fetch_all_post()
        elif choice == 8:
            await fetch_post_by_id()
        elif choice == 9:
            await update_post()
        elif choice == 10:
            await delete_post()
        elif choice == 0:
            break

    await engine.dispose()
asyncio.run(main())