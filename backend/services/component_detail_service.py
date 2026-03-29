from backend.utils.response.response_helper import pager
from backend.repository.component_detail_repository import ComponentDetailRepository
from backend.repository.device_detail_repository import DeviceDetailRepository
from backend.repository.component_device_repository import ComponentDeviceRepository
from backend.schema.component_detail_schema.component_detail_create_schema import ComponentDetailCreateSchema
from backend.schema.component_detail_schema.component_detail_response import ComponentDetailResponse
from backend.schema.component_detail_schema.component_detail_update_schema import ComponentDetailUpdateSchema
from backend.error.business_errors import ComponentDetailNotFound
from backend.utils.handle.hande_exception import handle_exceptions_class
from backend.entity.component_device_entity import ComponentDeviceEntity

@handle_exceptions_class
class ComponentDetailService:
    def __init__(self):
        self.component_detail_repository = ComponentDetailRepository()
        self.device_detail_repository = DeviceDetailRepository()
        self.component_device_repository = ComponentDeviceRepository()
    
    def create_component_detail(self, component_detail):
        component_detail_schema = ComponentDetailCreateSchema().load(component_detail)
        component_detail_entity = self.component_detail_repository.create_component_detail(component_detail_schema)
        
        # Auto-create component_device link
        device_detail = self.device_detail_repository.get_device_detail_by_id(component_detail_entity.device_detail_id)
        if device_detail:
            device_id = device_detail.device_id
            # Check if component_device already exists
            existing = self.component_device_repository.get_all_component_detail(component_id=component_detail_entity.component_id, device_id=device_id)
            if not existing[0]:  # if no results
                component_device = ComponentDeviceEntity(component_id=component_detail_entity.component_id, device_id=device_id)
                self.component_device_repository.create_component_device(component_device)
        
        return ComponentDetailResponse().dump(component_detail_entity)
    
    def get_component_detail_by_id(self, id):
        component_detail_entity = self.component_detail_repository.get_component_detail_by_id(id)
        return ComponentDetailResponse().dump(component_detail_entity)
    
    def update_component_detail(self, id, component_detail):
        component_detail_entity = self.component_detail_repository.get_component_detail_by_id(id)
        if not component_detail_entity:
            raise ComponentDetailNotFound()
        component_detail_schema = ComponentDetailUpdateSchema().load(component_detail)
        component_detail_entity = self.component_detail_repository.update_component_detail(id, component_detail_schema)
        return ComponentDetailResponse().dump(component_detail_entity)
    
    def delete_component_detail(self, id):
        component_detail_entity = self.component_detail_repository.get_component_detail_by_id(id)
        if not component_detail_entity:
            raise ComponentDetailNotFound()
        component_detail_entity = self.component_detail_repository.delete_component_detail(id)
        return ComponentDetailResponse().dump(component_detail_entity)
    
    def get_all_component_detail(
        self, page=1, limit=10,
        component_id=None, device_detail_id=None,
        status=None, buy_at=None,
    ):
        result, total = self.component_detail_repository.get_all_component_detail(
            page, limit, component_id, device_detail_id, status, buy_at
        )
        result_data = ComponentDetailResponse(many=True).dump(result)
        return pager(result_data, page, limit, total)
        
    def get_component_detail_by_device_detail_id(self, device_detail_id):
        component_detail_entities = self.component_detail_repository.get_component_detail_by_device_detail_id(device_detail_id)
        if not component_detail_entities:
            raise ComponentDetailNotFound()
        return ComponentDetailResponse(many=True).dump(component_detail_entities)
    
    def get_component_detail_by_component_id(self, component_id):
        component_detail_entities = self.component_detail_repository.get_component_detail_by_component_id(component_id)
        if not component_detail_entities:
            raise ComponentDetailNotFound()
        return ComponentDetailResponse(many=True).dump(component_detail_entities)
    