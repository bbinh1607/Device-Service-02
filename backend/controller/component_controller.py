from flask import Blueprint, request
from backend.services.component_service import ComponentService
from backend.utils.response.response_helper import api_response
from backend.utils.before_request.authenticate_request import authenticate_request

component_bp = Blueprint('component', __name__)
component_service = ComponentService()

@component_bp.before_request
def before_component_request():
    authenticate_request()

@component_bp.route('/create', methods=['POST'])
def create_component():
    data = request.get_json()
    result = component_service.create_component(data)
    return api_response(data = result)

@component_bp.route('/get-all', methods=['GET'])
def get_all_components():
    name = request.args.get("name")
    barcode = request.args.get("barcode")
    device_id = request.args.get("device_id")
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    result = component_service.get_all_components(
        page=page,
        limit=limit,
        name=name,
        barcode=barcode,
        device_id=device_id
    )
    return api_response(data=result)

@component_bp.route('/<id>', methods=['GET'])
def get_component(id):
    result = component_service.get_component_by_id(id)
    return api_response(data = result)

@component_bp.route('/<id>', methods=['PUT'])
def update_component(id):
    data = request.get_json()
    result = component_service.update_component(id, data)
    return api_response(data = result)

@component_bp.route('/<id>', methods=['DELETE'])
def delete_component(id):
    result = component_service.delete_component(id)
    return api_response(data = result)




