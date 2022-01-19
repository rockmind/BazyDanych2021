from northwind_db_api.database import SessionLocal
from northwind_db_api.models import Product


def get_employee(product_id: int):
    session = SessionLocal()
    return session.query(Product).filter(Product.product_id == product_id).first()