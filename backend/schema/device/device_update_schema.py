from marshmallow import Schema, fields, post_load
from backend.schema.__base_schema import BaseSchema
from backend.repository.device_repository import DeviceRepository


class DeviceUpdateSchema(BaseSchema):
    name = fields.String(required=False)
    description = fields.String(required=False)
    image_url = fields.String(required=False)
    barcode = fields.String(required=False)
    category_id = fields.Integer(required=False)

    class Meta:
        fields = ('name', 'description', 'image_url', 'barcode', 'category_id')
        
    @post_load
    def to_device_entity(self, data, **kwargs):
        return data
            # device_id = self.context.get('id')
            # # Lấy thông tin device từ repository
            # device_entity = DeviceRepository().get_device_by_id(device_id)
            
            # if device_entity is None:
            #     raise ValueError(f"Device with ID {device_id} not found.")
            # print("data", data)
            # # Cập nhật các trường trong device_entity với các giá trị từ data
            # for field, value in data.items():  # Duyệt qua 'data.items()'
            #     if value is not None:  # Nếu giá trị không phải null
            #         setattr(device_entity, field, value)  # Cập nhật giá trị

            # # Trả về dictionary của device_entity thay vì entity
            # device_dict = {field: getattr(device_entity, field) for field in data.keys()}  # Chỉ trả về các trường trong data

            # print("Updated device as dictionary:", device_dict)
            # return device_dict  # Trả về dictionary của device_entity chỉ chứa các trường đã cập nhật
            
    

 
