from typing import Optional

from northwind_db_api.database import SessionLocal
from northwind_db_api.models import Customer
from northwind_db_api.schemas import CustomerWithOrders as CustomerSchema

session = SessionLocal()


def create_customer(customer: CustomerSchema):
    db_customer = Customer(
        customer_id=customer.customer_id,
        company_name=customer.contact_name,
        contact_name=customer.contact_name,
        contact_title=customer.contact_title,
        address=customer.address,
        city=customer.city,
        region=customer.region,
        postal_code=customer.postal_code,
        country=customer.country,
        phone=customer.phone,
        fax=customer.fax
    )
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)  # po co to?
    return db_customer


def get_customer(customer_id: str) -> Optional[CustomerSchema]:
    customer = session.query(Customer).filter(Customer.customer_id == customer_id).first()
    return CustomerSchema.from_orm(customer)


def update_customer(customer: CustomerSchema):
    db_customer = Customer(
        customer_id=customer.customer_id,
        company_name=customer.contact_name,
        contact_name=customer.contact_name,
        contact_title=customer.contact_title,
        address=customer.address,
        city=customer.city,
        region=customer.region,
        postal_code=customer.postal_code,
        country=customer.country,
        phone=customer.phone,
        fax=customer.fax
    )
    session.refresh(db_customer)
    session.commit()
    # session.refresh(db_customer)
    return db_customer  # TODO:to check


def delete_customer(customer_id: str):
    customer = get_customer(customer_id)
    session.delete(customer)
    try:
        session.commit()
    except Exception:
        return False
    return True
