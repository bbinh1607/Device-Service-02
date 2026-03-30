from flask import Blueprint, request
from backend.services.device_detail_service import DeviceDetailService
from backend.utils.response.response_helper import api_response
from backend.utils.before_request.authenticate_request import authenticate_request

device_detail_bp = Blueprint('device_detail', __name__)
device_detail_service = DeviceDetailService()

@device_detail_bp.before_request
def before_device_detail_request():
    authenticate_request()


@device_detail_bp.route('/create', methods=['POST'])
def create_device_detail():
    data = request.json
    result = device_detail_service.create_device_detail(data)
    return api_response(data = result)

@device_detail_bp.route('/get-all', methods=['GET'])
def get_all_device_detail():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    result = device_detail_service.get_all_device_detail(
        page=page,
        limit=limit,
        name=request.args.get("name"),
        create_at=request.args.get("createAt"),
        device_id=request.args.get("device_id"),
        area=request.args.get("area"),
        buy_at=request.args.get("buyAt"),
        warranty=request.args.get("warranty"),
        status=request.args.get("status"),
        component_id=request.args.get("component_id"),
    )
    return api_response(data=result)

@device_detail_bp.route('/get/<id>', methods=['GET'])
def get_device_detail_by_id(id):
    result = device_detail_service.get_device_detail_by_id(id)
    return api_response(data = result)

@device_detail_bp.route('/update/<id>', methods=['PUT'])
def update_device_detail(id):
    data = request.json
    result = device_detail_service.update_device_detail(id, data)
    return api_response(data = result)

