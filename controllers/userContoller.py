from fastapi import Body, Path
import redis
from dotenv import load_dotenv
from pydantic import BaseModel

import os



load_dotenv()

redis_client = redis.Redis(
    host='193.3.298.206',
    port=os.getenv("REDIS_PORT"),
    db=os.getenv("REDIS_DB"),
    username=os.getenv("REDIS_USER"),
    password=os.getenv("REDIS_PASSWORD")
)

class BodyItem(BaseModel):
    name: str
    surname: str
    patronymic: str

class UserController:
    def __init__(self):
        if redis_client:
            print("connect to db")
        else:
            print("error connecting to database")

    async def createUser(self, body: BodyItem = Body()):
        generate_id = 0
        generate_id+=1
        name = await redis_client.hset("user:" + str(generate_id), "name", body.get("name"))
        surname = await redis_client.hset("user:" + str(generate_id), "surname", body.get("surname"))
        patronymic = await redis_client.hset("user:" + str(generate_id), "patronymic", body.get("patronymic"))
        redis_client.close()
        return (
            generate_id,
            name,
            surname,
            patronymic    
        )

    async def getUserById(user_id = Path()):
        user = await redis_client.hgetall("user:"+str(user_id))
        redis_client.close()
        return user
    
    async def UpdateUser(user_id: str = Path(), body: BodyItem = Body()):
        name = await redis_client.hset("user:" + user_id, "name", body.get("name"))
        surname = await redis_client.hset("user:" + user_id, "surname", body.get("surname"))
        patronymic = await redis_client.hset("user:" + user_id, "patronymic", body.get("patronymic"))
        redis_client.close()
        return (
            user_id,
            name,
            surname,
            patronymic    
        )

    async def deleteUser(user_id: str = Path()):
        delete_user = await redis_client.hdel("user:"+user_id)
        redis_client.close()
        return delete_user