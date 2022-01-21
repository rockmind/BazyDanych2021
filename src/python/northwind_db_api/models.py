from sqlalchemy import Column, SmallInteger, String, LargeBinary, Table, ForeignKey, Date, Float, Integer
from sqlalchemy.orm import relationship

from northwind_db_api.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(SmallInteger, primary_key=True, index=True)
    category_name = Column(String)
    description = Column(String)
    picture = Column(LargeBinary)

    product = relationship("Product", back_populates="category")


# class CustomerCustomerDemo(Base):       # TODO
#     __tablename__ = "customer_customer_demo"
#
#     customer_id = Column()
#
#
# class CustomerDemographics(Base):
#     __tablename__ = "customer_demographics"
#
#
class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(String, primary_key=True, index=True)
    company_name = Column(String)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)

    orders = relationship("Order", back_populates="customer")


# zmienna zamiast klasy odwzorowującej tabelę pośredniczącą
employee_territory_association = Table("employee_territories", Base.metadata,
    Column("employee_id", ForeignKey("employees.employee_id"), primary_key=True),
    Column("territory_id", ForeignKey("territories.territory_id"), primary_key=True)
)


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(SmallInteger, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    title = Column(String)
    title_of_courtesy = Column(String)
    birth_date = Column(Date)
    hire_date = Column(Date)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    home_phone = Column(String)
    extension = Column(String)
    photo = Column(LargeBinary)
    notes = Column(String)
    reports_to = Column(SmallInteger, ForeignKey("employees.employee_id"))  #klucz obcy do siebie samej
    photo_path = Column(String)

    territory = relationship("Territory", secondary=employee_territory_association, back_populates="employee")
    # employee_reporte = relationship("Employee", back_populates="reports_to")  TODO: self-reference
    order = relationship("Order", back_populates="employee")


class OrderDetail(Base):
    __tablename__ = "order_details"

    order_id = Column(SmallInteger, ForeignKey("orders.order_id"), primary_key=True, index=True)
    product_id = Column(SmallInteger, ForeignKey("products.product_id"), primary_key=True, index=True)
    unit_price = Column(Float)
    quantity = Column(SmallInteger)
    discount = Column(Float)

    order = relationship("Order", back_populates="order_detail")
    product = relationship("Product", back_populates="order_detail")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(SmallInteger, primary_key=True, index=True)
    customer_id = Column(String, ForeignKey("customers.customer_id"))
    employee_id = Column(SmallInteger, ForeignKey("employees.employee_id"))
    order_date = Column(Date)
    required_date = Column(Date)
    shipped_date = Column(Date)
    ship_via = Column(SmallInteger, ForeignKey("shippers.shipper_id"))
    freight = Column(Float)
    ship_name = Column(String)
    ship_address = Column(String)
    ship_city = Column(String)
    ship_region = Column(String)
    ship_postal_code = Column(String)
    ship_country = Column(String)

    order_detail = relationship("OrderDetail", cascade="all,delete", back_populates="order")
    customer = relationship("Customer", back_populates="orders")
    employee = relationship("Employee", back_populates="order")
    shipper = relationship("Shipper", back_populates="order")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(SmallInteger, primary_key=True, index=True)
    product_name = Column(String)
    supplier_id = Column(SmallInteger, ForeignKey("suppliers.supplier_id"))
    category_id = Column(SmallInteger, ForeignKey("categories.category_id"))
    quantity_per_unit = Column(String)
    unit_price = Column(Float)
    units_in_stock = Column(SmallInteger)
    units_on_order = Column(SmallInteger)
    reorder_level = Column(SmallInteger)
    discontinued = Column(Integer)

    order_detail = relationship("OrderDetail", back_populates="product")
    supplier = relationship("Supplier", back_populates="product")
    category = relationship("Category", back_populates="product")


class Region(Base):
    __tablename__ = "region"

    region_id = Column(SmallInteger, primary_key=True, index=True)
    region_description = Column(String)

    territory = relationship("Territory", back_populates="region")


class Shipper(Base):
    __tablename__ = "shippers"

    shipper_id = Column(SmallInteger, primary_key=True, index=True)
    company_name = Column(String)
    phone = Column(String)

    order = relationship("Order", back_populates="shipper")


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(SmallInteger, primary_key=True, index=True)
    company_name = Column(String)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)
    homepage = Column(String)

    product = relationship("Product", back_populates="supplier")


class Territory(Base):
    __tablename__ = "territories"

    territory_id = Column(String, primary_key=True, index=True)
    territory_description = Column(String)
    region_id = Column(SmallInteger, ForeignKey("region.region_id"))

    employee = relationship("Employee", secondary=employee_territory_association, back_populates="territory")
    region = relationship("Region", back_populates="territory")


# class USStates(Base):
#     __tablename__ = "us_states"  # wydaje się nie potrzebne


