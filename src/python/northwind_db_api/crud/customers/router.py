from typing import List
from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session

from northwind_db_api.database import DBErrorObjectNotExists, get_db
from northwind_db_api.crud import customers as crud
from northwind_db_api.schemas import Customer, CustomerWithOrders, Order

customers_crud_router = APIRouter(prefix="/customers")


@customers_crud_router.get("/", response_model=List[Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_customers(db, skip=skip, limit=limit)
    return users


@customers_crud_router.get("/{customer_id}", response_model=Customer)
def read_customer(customer_id: str, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@customers_crud_router.get("/{customer_id}/orders/", response_model=List[Order])
def read_customers_items(customer_id: str, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer = CustomerWithOrders.from_orm(db_customer)
    return customer.orders


@customers_crud_router.post("/", response_model=Customer, status_code=201)
def create_customer(customer: Customer, db: Session = Depends(get_db)):
    if crud.get_customer_by_company_name(db, company_name=customer.company_name):
        raise HTTPException(status_code=400, detail="Customer with this company name already registered")

    if crud.get_customer_by_id(db, customer_id=customer.customer_id):
        raise HTTPException(status_code=400, detail="Customer with this customer_id already registered")
    return crud.create_customer(db_session=db, customer=customer)


@customers_crud_router.patch("/{customer_id}", response_model=Customer, status_code=201)
@customers_crud_router.put("/{customer_id}", response_model=Customer, status_code=201)
def update_customer(customer_id: str, customer: Customer, db: Session = Depends(get_db)):
    if customer.customer_id:
        raise HTTPException(status_code=400, detail="Changing customer_id is forbidden")
    customer.customer_id = customer_id
    try:
        crud.update_customer(db_session=db, customer=customer)
    except DBErrorObjectNotExists:
        raise HTTPException(status_code=400, detail="Customer with this customer_id dose not exits")

    return customer


@customers_crud_router.delete("/{customer_id}", status_code=204)
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(status_code=400, detail="Customer with this customer_id dose not exits")
    crud.delete_customer(db_session=db, customer=db_customer)
