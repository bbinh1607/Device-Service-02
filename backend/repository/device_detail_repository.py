from sqlalchemy import func
from backend.extensions import db
from backend.entity.device_detail_entity import DeviceDetailEntity
from backend.utils.handle.hande_exception import handle_exceptions_repository_class

@handle_exceptions_repository_class
class DeviceDetailRepository:
    def __init__(self):
        self.db = db.session

    def create_device_detail(self, device_detail):
        self.db.add(device_detail)
        self.db.commit()
        return device_detail
    
    def get_device_detail_by_id(self, id):
        return self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id).first()

    def update_device_detail(self, id, device_detail): 
        query = self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id)
        query.update(device_detail)
        self.db.commit()
        entity = query.first()
        self.db.refresh(entity)
        return entity

    
    def delete_device_detail(self, id):
        device_detail_data = self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id).first()
        self.db.delete(device_detail_data)
        self.db.commit()
        return device_detail_data
    
    
    def get_all_device_detail(self, page, limit, name=None, create_at=None, device_id=None, area=None, buy_at=None, warranty=None, status=None):
        query = self.db.query(DeviceDetailEntity)

        if name:
            query = query.filter(query.DeviceEntity.name.ilike(f"%{name}%"))
        if create_at:
            query = query.filter(func.date(DeviceDetailEntity.created_at) == create_at)
        if device_id:
            query = query.filter(DeviceDetailEntity.device_id == device_id)
        if area:
            query = query.filter(DeviceDetailEntity.area.ilike(f"%{area}%"))
        if buy_at:
            query = query.filter(func.date(DeviceDetailEntity.buyAt) == buy_at)
        if warranty:
            query = query.filter(func.date(DeviceDetailEntity.warranty) == warranty)
        if status:
            query = query.filter(DeviceDetailEntity.status.ilike(f"%{status}%"))

        total = query.count()

        results = query.order_by(DeviceDetailEntity.created_at.desc()) \
                    .offset((page - 1) * limit) \
                    .limit(limit).all()

        return results, total

    
    
    def get_device_detail_by_id(self, id):
        return self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id).first()
