from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from ._base_entity import BaseEntity

class DeviceEntity(BaseEntity):
    __tablename__ = 'device'

    name = Column(String, nullable=False,unique=True)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    barcode = Column(String, nullable=True,unique=True)
    category_id = Column(String, ForeignKey('categorie.id'), nullable=False)
    
    
    category = relationship('CategoryEntity', backref='devices')