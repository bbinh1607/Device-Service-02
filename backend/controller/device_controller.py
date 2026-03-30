from flask import Blueprint, request
from backend.services.device_service import DeviceService
from backend.utils.response.response_helper import api_response
from backend.utils.before_request.authenticate_request import authenticate_request

device_bp = Blueprint("device", __name__)
device_service = DeviceService()


@device_bp.before_request
def before_device_request():
    authenticate_request()

@device_bp.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    result = device_service.create_device(data)
    return api_response(data = result)


@device_bp.route("/get-all", methods=["GET"])
def get_all():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    name = request.args.get("name", "")
    create_at = request.args.get("createAt", None)
    category_id = request.args.get("category_id","")
    result = device_service.get_all_devices(page, limit, name=name, create_at=create_at, category_id=category_id)
    return api_response(data=result)

@device_bp.route("/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = device_service.update_device(id, data)
    return api_response(data = result)

@device_bp.route("/<id>", methods=["DELETE"]) 
def delete(id):
    result = device_service.delete_device(id)
    return api_response(data = result)

@device_bp.route("/<id>", methods=["GET"])
def get(id):
    result = device_service.get_device_by_id(id)
    return api_response(data = result)

