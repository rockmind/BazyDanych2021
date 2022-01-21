from fastapi import FastAPI
from northwind_db_api.crud.customers.router import customers_crud_router

web_app = FastAPI(title='NorthWindDbApi')
web_app.include_router(customers_crud_router)
