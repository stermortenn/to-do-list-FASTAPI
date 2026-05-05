from fastapi import FastAPI
from routers import auth_router, user_router, task_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(task_router.router)

@app.get("/")
def root():
    return {"status": "ok"}
