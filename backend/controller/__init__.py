from flask import Blueprint, render_template
from backend.error.error_handlers import error_bp
from backend.controller.category_controller import category_bp
from backend.controller.device_controller import device_bp
from backend.controller.component_controller import component_bp
from backend.controller.component_detail_controller import component_detail_bp
from backend.controller.device_detail_controller import device_detail_bp

main_bp = Blueprint("main", __name__)

main_bp.register_blueprint(error_bp, url_prefix="/errors")
main_bp.register_blueprint(category_bp, url_prefix="/categories")
main_bp.register_blueprint(device_bp, url_prefix="/devices")
main_bp.register_blueprint(device_detail_bp, url_prefix="/device-details")
main_bp.register_blueprint(component_bp, url_prefix="/components")
main_bp.register_blueprint(component_detail_bp, url_prefix="/component-details")

def register_controllers(app):
    app.register_blueprint(main_bp)


@main_bp.route("/")
def home():
    return render_template("home.html")