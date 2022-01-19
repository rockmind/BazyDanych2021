from northwind_db_api.database import SessionLocal
from northwind_db_api.models import Supplier


def get_employee(supplier_id: int):
    session = SessionLocal()
    return session.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()