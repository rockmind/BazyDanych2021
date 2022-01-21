from typing import Optional, TYPE_CHECKING, List

from northwind_db_api.database import DBErrorObjectNotExists
from northwind_db_api.models import Order as OrderModel
from northwind_db_api.schemas import Order as OrderSchema

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def create_order(db_session: 'Session', order: OrderSchema):
    db_order = OrderModel(**order.dict())
    db_session.add(db_order)
    db_session.commit()
    db_session.refresh(db_order)
    return db_order


def get_orders(db_session: 'Session', skip: int = 0, limit: int = 100) -> List[OrderModel]:
    return db_session.query(OrderModel).offset(skip).limit(limit).all()


def get_order_by_id(db_session: 'Session', order_id: str) -> Optional[OrderModel]:
    order = db_session.query(OrderModel).filter(OrderModel.order_id == order_id).first()
    return order


def get_order_by_company_name(db_session: 'Session', company_name: str) -> Optional[OrderModel]:
    order = db_session.query(OrderModel).filter(OrderModel.company_name == company_name).first()
    return order


def update_order(db_session: 'Session', order: OrderSchema):
    db_order = get_order_by_id(db_session, order_id=order.order_id)
    try:
        db_session.query(OrderModel).filter(OrderModel.order_id == db_order.order_id)\
                                       .update(order.dict())
    except AttributeError:
        db_session.rollback()
        raise DBErrorObjectNotExists
    else:
        db_session.commit()


def delete_order(db_session: 'Session', order: OrderModel):
    db_session.delete(order)
    db_session.commit()
