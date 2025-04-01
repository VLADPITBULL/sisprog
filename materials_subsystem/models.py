from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from db import Base

material_supplier = Table(
    'material_supplier',
    Base.metadata,
    Column('material_id', Integer, ForeignKey('materials.id')),
    Column('supplier_id', Integer, ForeignKey('suppliers.id'))
)

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    stock_qty = Column(Integer)
    min_stock = Column(Integer)
    unit = Column(String)
    image_url = Column(String)
    suppliers = relationship("Supplier", secondary=material_supplier, back_populates="materials")

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    materials = relationship("Material", secondary=material_supplier, back_populates="suppliers")
