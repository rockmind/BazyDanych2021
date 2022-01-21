from typing import List
from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session

from northwind_db_api.database import DBErrorObjectNotExists, get_db
from northwind_db_api.crud import orders as crud
from northwind_db_api.schemas import Order

orders_crud_router = APIRouter(prefix="/orders")


@orders_crud_router.get("/", response_model=List[Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@orders_crud_router.get("/{order_id}", response_model=Order)
def read_order(order_id: str, db: Session = Depends(get_db)):
    db_order = crud.get_order_by_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@orders_crud_router.post("/", response_model=Order, status_code=201)
def create_order(order: Order, db: Session = Depends(get_db)):
    if crud.get_order_by_id(db, order_id=order.order_id):
        raise HTTPException(status_code=400, detail="Order with this order_id already registered")
    return crud.create_order(db_session=db, order=order)


@orders_crud_router.patch("/{order_id}", response_model=Order, status_code=201)
@orders_crud_router.put("/{order_id}", response_model=Order, status_code=201)
def update_order(order_id: str, order: Order, db: Session = Depends(get_db)):
    if order.order_id:
        raise HTTPException(status_code=400, detail="Changing order_id is forbidden")
    order.order_id = order_id
    try:
        crud.update_order(db_session=db, order=order)
    except DBErrorObjectNotExists:
        raise HTTPException(status_code=400, detail="Order with this order_id dose not exits")

    return order


@orders_crud_router.delete("/{order_id}", status_code=204)
def delete_order(order_id: str, db: Session = Depends(get_db)):
    db_order = crud.get_order_by_id(db, order_id=order_id)
    if not db_order:
        raise HTTPException(status_code=400, detail="Order with this order_id dose not exits")
    crud.delete_order(db_session=db, order=db_order)
