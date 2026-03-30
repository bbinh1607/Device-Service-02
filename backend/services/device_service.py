from backend.repository.device_repository import DeviceRepository
from backend.repository.category_repository import CategoryRepository
from backend.schema.device.device_reponse import DeviceResponse
from backend.schema.device.device_create_schema import DeviceCreateSchema
from backend.schema.device.device_update_schema import DeviceUpdateSchema
from backend.error.business_errors import DeviceNotFound, CategoryNotFound
from backend.utils.handle.hande_exception import handle_exceptions_class
from backend.client.file_service_client import FileServiceClient
from backend.utils.response.response_helper import pager

@handle_exceptions_class
class DeviceService:
    def __init__(self):
        self.device_repository = DeviceRepository()
        self.category_repository = CategoryRepository()
        self.file_service_client = FileServiceClient()
        

    def create_device(self, data):
        device =  DeviceCreateSchema().load(data)
        if device.category_id is not None:
            category = self.category_repository.get_category_by_id(device.category_id)
            if category is None:
                raise CategoryNotFound()
        device = self.device_repository.create_device(device)
        return DeviceResponse().dump(device)
        
    def get_device_by_id(self, id):
        device = self.device_repository.get_device_by_id(id)
        return DeviceResponse().dump(device)
    
    def get_all_devices(self, page=1, limit=100, name=None, create_at=None, category_id=None):
        result, total = self.device_repository.get_all_devices(page, limit, name, create_at, category_id)
        results = DeviceResponse(many=True).dump(result)
        return pager(results=results, page=page, limit=limit, total=total)

        
    def update_device(self, id , data):
        device = self.device_repository.get_device_by_id(id)
        if device is None:
            raise DeviceNotFound()
        device_update = DeviceUpdateSchema().load(data)
        device = self.device_repository.update_device(id, device_update)
        return DeviceResponse().dump(device)
    
    def delete_device(self, id):
        device = self.device_repository.get_device_by_id(id)
        if device is None:
            raise DeviceNotFound()
        device = self.device_repository.delete_device(id)
        return True
        