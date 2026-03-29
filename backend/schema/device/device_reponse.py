from marshmallow import fields, post_dump, pre_dump
from backend.schema.__base_schema import BaseSchema
from backend.schema.category.category_reponse import CategoryResponse
from backend.client.file_service_client import FileServiceClient
from backend.schema.component.component_reponse import ComponentResponse
from backend.repository.component_device_repository import ComponentDeviceRepository
from backend.entity.component_device_entity import ComponentDeviceEntity
from backend.entity.device_entity import DeviceEntity

class DeviceResponse(BaseSchema):
    name = fields.String()
    description = fields.String()
    barcode = fields.String()
    image_url = fields.String()
    file = fields.Raw(dump_only= True)
    category = fields.Nested(CategoryResponse, dump_only=True)
    
    list_component = fields.Nested(ComponentResponse, many=True, dump_only=True)

    @pre_dump
    def handle_object(self, data, **kwargs):
        list_component_device = ComponentDeviceRepository().get_all_component_detail(device_id=data.id)
        list_component = []
        for item in list_component_device[0]:
            list_component.append(item.component)
        data.list_component = list_component if list_component else []

        return data


    @post_dump
    def include_file(self, data, **kwargs):
        if 'image_url' in data and data['image_url'] is not None:
            file_data = FileServiceClient().get_file_by_id(data['image_url'])
            data['file'] = file_data
            del data['image_url']
        
        return data
