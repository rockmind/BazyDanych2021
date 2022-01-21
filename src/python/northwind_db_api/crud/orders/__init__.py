from typing import Optional, TYPE_CHECKING, List

from northwind_db_api.database import DBErrorObjectNotExists
from northwind_db_api.models import Order as OrderModel, Date
from northwind_db_api.schemas import Order as OrderSchema

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def create_order(db_session: 'Session', order: OrderSchema):
    db_order = OrderModel(**order.dict())
    db_session.add(db_order)
    db_session.commit()
    db_session.refresh(db_order)
    return db_order


def get_orders(
        db_session: 'Session',
        skip: int = 0,
        limit: int = 100,
        customer_id: str = None,
        employee_id: str = None,
        date_from: Date = None,
        date_to: Date = None,
        ship_via: str = None,
) -> List[OrderModel]:
    db_query = db_session.query(OrderModel)
    if customer_id:
        db_query = db_query.filter(OrderModel.customer_id == customer_id)
    if employee_id:
        db_query = db_query.filter(OrderModel.employee_id == employee_id)
    if ship_via:
        db_query = db_query.filter(OrderModel.ship_via == ship_via)
    if date_from:
        db_query = db_query.filter(OrderModel.order_date >= date_from)
    if date_to:
        db_query = db_query.filter(OrderModel.order_date <= date_to)

    return db_query.offset(skip).limit(limit).all()


def get_order_by_id(db_session: 'Session', order_id: int) -> Optional[OrderModel]:
    order = db_session.query(OrderModel).filter(OrderModel.order_id == order_id).first()
    return order


def update_order(db_session: 'Session', order: OrderSchema):
    db_order = get_order_by_id(db_session, order_id=order.order_id)
    try:
        db_session.query(OrderModel).filter(OrderModel.order_id == db_order.order_id).update(order.dict())
    except AttributeError:
        db_session.rollback()
        raise DBErrorObjectNotExists
    else:
        db_session.commit()


def delete_order(db_session: 'Session', order: OrderModel):
    db_session.delete(order)
    db_session.commit()
