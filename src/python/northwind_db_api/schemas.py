from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class BaseCustomer(BaseModel):
    customer_id: str
    company_name: str
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


class Customer(BaseCustomer):

    orders: List['BaseOrder'] = []


class BaseOrder(BaseModel):
    order_id: Optional[int]
    customer_id: Optional[str]
    employee_id: Optional[int]
    order_date: Optional[datetime]
    required_date: Optional[datetime]
    shipped_date: Optional[datetime]
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


Customer.update_forward_refs()


class Order(BaseOrder):
    customer: Optional['Customer']

