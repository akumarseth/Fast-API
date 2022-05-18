from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from internal import admin
from routers import items, users


app = FastAPI(
    dependencies=[Depends(get_query_token)],
    title="Monitoring App",
    description="API Docs for Monitoring App",
    version="0.0.1",
    terms_of_service="http://tredence.com.com",
    contact={
        "name": "Abhishek Kumar",
        "url": "http://x-force.example.com/contact/",
        "email": "abhishek.kumar1@tredence.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
