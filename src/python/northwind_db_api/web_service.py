from fastapi import FastAPI

web_app = FastAPI(title='NorthWindDbApi')


@web_app.get("/")
async def root():
    return {"message": "Hello World"}


