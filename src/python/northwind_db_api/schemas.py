from __future__ import annotations
from datetime import date
from typing import List, Optional

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):

    def json(self, *args, **kwargs):
        kwargs.pop('exclude_none', None)
        return super().json(*args, **kwargs, exclude_none=True)

    def dict(self, *args, **kwargs):
        kwargs.pop('exclude_none', None)
        return super().dict(*args, **kwargs, exclude_none=True)


class Customer(BaseModel):
    customer_id: Optional[str]
    company_name: Optional[str]
    contact_name: Optional[str]
    contact_title: Optional[str]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    fax: Optional[str]

    class Config:
        orm_mode = True


class CustomerWithOrders(Customer):
    orders: List[Order] = []


class Order(BaseModel):
    order_id: Optional[str]
    customer_id: Optional[str]
    employee_id: Optional[int]
    order_date: Optional[date]
    required_date: Optional[date]
    shipped_date: Optional[date]
    ship_via: Optional[int]
    freight: Optional[float]
    ship_name: Optional[str]
    ship_address: Optional[str]
    ship_city: Optional[str]
    ship_region: Optional[str]
    ship_postal_code: Optional[str]
    ship_country: Optional[str]

    class Config:
        orm_mode = True


class OrderWithCustomer(Order):
    customer: Optional[Customer]


CustomerWithOrders.update_forward_refs()
OrderWithCustomer.update_forward_refs()
