from typing import Optional, TYPE_CHECKING, List

from northwind_db_api.database import DBErrorObjectNotExists
from northwind_db_api.models import Customer as CustomerModel
from northwind_db_api.schemas import Customer as CustomerSchema

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def create_customer(db_session: 'Session', customer: CustomerSchema):
    db_customer = CustomerModel(**customer.dict())
    db_session.add(db_customer)
    db_session.commit()
    db_session.refresh(db_customer)  # po co to?
    return db_customer


def get_customers(db_session: 'Session', skip: int = 0, limit: int = 100) -> List[CustomerModel]:
    return db_session.query(CustomerModel).offset(skip).limit(limit).all()


def get_customer_by_id(db_session: 'Session', customer_id: str) -> Optional[CustomerModel]:
    customer = db_session.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
    return customer


def get_customer_by_company_name(db_session: 'Session', company_name: str) -> Optional[CustomerModel]:
    customer = db_session.query(CustomerModel).filter(CustomerModel.company_name == company_name).first()
    return customer


def update_customer(db_session: 'Session', customer: CustomerSchema):
    db_customer = get_customer_by_id(db_session, customer_id=customer.customer_id)
    try:
        db_session.query(CustomerModel).filter(CustomerModel.customer_id == db_customer.customer_id)\
                                       .update(customer.dict())
    except AttributeError:
        db_session.rollback()
        raise DBErrorObjectNotExists
    else:
        db_session.commit()


def delete_customer(db_session: 'Session', customer: CustomerModel):
    db_session.delete(customer)
    db_session.commit()
