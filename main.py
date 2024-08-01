from fastapi import Body, FastAPI

from routes.userRoutes import router


app = FastAPI()

app.include_router(router)