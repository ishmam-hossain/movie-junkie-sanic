from sanic import Blueprint
from .views import RegisterAPI, TestAPI


auth_bp = Blueprint('auth', url_prefix='/auth')
# auth_bp.add_route(LoginAPI.as_view(), '/login')
# auth_bp.add_route(LogoutAPI.as_view(), '/logout')
auth_bp.add_route(RegisterAPI.as_view(), '/register')
# auth_bp.add_route(RefreshAPI.as_view(), '/refresh')
auth_bp.add_route(TestAPI.as_view(), '/test')
