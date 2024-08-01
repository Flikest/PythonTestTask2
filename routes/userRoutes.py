from fastapi import APIRouter, Body, Path, Request

from controllers.userContoller import UserController

userController = UserController()

router = APIRouter()

@router.post("/createuser")
async def createUser(body: Request):
    return await userController.createUser(body)

@router.get("/getuserbyid")
async def getUserById(user_id: str = Path()):
    return await UserController.getUserById(user_id)

@router.put("/updateuser")
async def updateUser(body: Request, user_id: str = Path()):
    return await userController.UpdateUser(user_id, body)

@router.delete("/deleteuser")
async def deleteUser(user_id: str = Path()):
    return await userController.deleteUser(user_id)