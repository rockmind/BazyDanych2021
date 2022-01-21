from typing import Optional
from sqlalchemy.orm import Session
from northwind_db_api.database import SessionLocal
from northwind_db_api.models import Order
from northwind_db_api.schemas import OrderWithCustomer as OrderWithCustomerSchema, Order as OrderSchema

session = SessionLocal()


def create_order(db_session: Session, order: OrderWithCustomerSchema):
    db_order = Order(
        order_id=order.order_id,
        customer_id=order.customer_id,
        employee_id=order.employee_id,
        order_date=order.order_date,
        required_date=order.required_date,
        shipped_date=order.shipped_date,
        ship_via=order.ship_via,
        freight=order.freight,
        ship_name=order.ship_name,
        ship_address=order.ship_address,
        ship_city=order.ship_city,
        ship_region=order.ship_region,
        ship_postal_code=order.ship_postal_code,
        ship_country=order.ship_country,
    )
    db_session.add(db_order)
    db_session.commit()
    db_session.refresh(db_order)
    return db_order


def get_order(db_session: Session, order_id: str) -> Order:
    order = db_session.query(Order).filter(Order.customer_id == order_id).first()
    return OrderWithCustomerSchema.from_orm(order)


def update_order(db_session: Session, order: OrderSchema):
    order_dict = order.dict(exclude=None)
    db_order = db_session.query(Order).filter(Order.customer_id == order.order_id).first()
    if db_order:
        db_order = OrderWithCustomerSchema.from_orm(order)
    # db_order = Order(
    #     customer_id=customer.customer_id,
    #     company_name=customer.contact_name,
    #     contact_name=customer.contact_name,
    #     contact_title=customer.contact_title,
    #     address=customer.address,
    #     city=customer.city,
    #     region=customer.region,
    #     postal_code=customer.postal_code,
    #     country=customer.country,
    #     phone=customer.phone,
    #     fax=customer.fax
    # )
    # session.refresh(db_order)
    # session.commit()
    # # session.refresh(db_order)
    return db_order  # TODO:to check

