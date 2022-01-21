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


class OrderWithOrderDetails(Order):
    orderDetails: List[OrderDetail] = []


class OrderDetail(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: int
    discount: float

    class Config:
        orm_mode = True


class OrderDetailWithOrder(OrderDetail):
    order: Order


class OrderDetailWithProduct(OrderDetail):
    product: Product


class Product(BaseModel):
    product_id: int
    product_name: str
    supplier_id: Optional[int]
    category_id: Optional[int]
    quantity_per_unit: Optional[str]
    unit_price: Optional[float]
    units_in_stock: Optional[int]
    units_on_order: Optional[int]
    reorder_level: Optional[int]
    discontinued: int

    class Config:
        orm_mode = True


class ProductWithOrderDetail(Product):
    orderDetails: List[OrderDetail] = []


class ProductWithSupplier(Product):
    supplier: Optional[Supplier]


class ProductWithCategory(Product):
    category: Optional[Category]


class Category(BaseModel):
    category_id: int
    category_name: str
    description: Optional[str]
    picture: Optional[bytes]

    class Config:
        orm_mode = True


class CategoryWithProducts(Category):
    products: List[Product] = []


class Supplier(BaseModel):
    supplier_id: int
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
    homepage: Optional[str]

    class Config:
        orm_mode = True


class SupplierWithProducts(Supplier):
    products: List[Product] = []


CustomerWithOrders.update_forward_refs()
OrderWithCustomer.update_forward_refs()
OrderWithOrderDetails.update_forward_refs()
OrderDetailWithOrder.update_forward_refs()
OrderDetailWithProduct.update_forward_refs()
ProductWithOrderDetail.update_forward_refs()
ProductWithSupplier.update_forward_refs()
ProductWithCategory.update_forward_refs()
CategoryWithProducts.update_forward_refs()
SupplierWithProducts.update_forward_refs()
