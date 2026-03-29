from backend.extensions import db
from backend.utils.handle.hande_exception import handle_exceptions_repository_class
from backend.entity.component_device_entity import ComponentDeviceEntity
from sqlalchemy.orm import joinedload
from sqlalchemy import func

@handle_exceptions_repository_class
class ComponentDeviceRepository:
    def __init__(self):
        self.db = db.session

    def create_component_device(self, component_device):
        """Tạo một component_device mới và commit vào database."""
        self.db.add(component_device)
        self.db.commit()
        return component_device

    def get_component_detail_by_id(self, id):
        """Lấy chi tiết của component_device theo ID."""
        return self.db.query(ComponentDeviceEntity).filter(ComponentDeviceEntity.id == id).first()

    def get_all_component_detail(self, component_id=None, device_id=None,):
        """Lấy danh sách tất cả component_device với phân trang và các tham số tùy chọn như component_id, device_id."""
        query = self.db.query(ComponentDeviceEntity)

        if component_id:
            query = query.filter(ComponentDeviceEntity.component_id == component_id)
        if device_id:
            query = query.filter(ComponentDeviceEntity.device_id == device_id)

        total = query.count()

        results = query.order_by(ComponentDeviceEntity.created_at.desc()).all()

        return results, total

    def update_component_device(self, id, component_device_data):
        """Cập nhật một component_device và trả về entity đã được cập nhật."""
        query = self.db.query(ComponentDeviceEntity).filter(ComponentDeviceEntity.id == id)
        query.update(component_device_data)
        self.db.commit()
        entity = query.first()
        self.db.refresh(entity)
        return entity

    def delete_component_device(self, id):
        """Xóa một component_device theo ID và trả về entity đã bị xóa."""
        component_device = self.db.query(ComponentDeviceEntity).filter(ComponentDeviceEntity.id == id).first()
        if component_device:
            self.db.delete(component_device)
            self.db.commit()
        return component_device

   