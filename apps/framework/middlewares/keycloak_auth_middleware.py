import logging

from apps.framework.constants import AUTH_TOKEN_HEADER_NAME
from apps.framework.utils.keycloak_client import KeyCloakClient
from apps.framework.utils.web_utils import WebUtils
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status


class KeyCloakAuthMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.logger = logging.getLogger(__name__)
        self.keyclock_client = KeyCloakClient()

    def set_userinfo(self, request, token_info):
        """设置用户信息"""
        request.userinfo = {
            "username": token_info.get("username", ""),
            "email": token_info.get("email", ""),
        }

    def process_view(self, request, view, args, kwargs):

        # 只对/api的路径进行处理，其他路径默认放行
        if not request.path.startswith("/api") or request.path.startswith("/api/public/"):
            return None

        token = request.META.get(AUTH_TOKEN_HEADER_NAME)
        if token is None:
            return WebUtils.response_error(error_message="请提供Token", status=status.HTTP_401_UNAUTHORIZED)

        is_active, token_info = self.keyclock_client.token_is_valid(token)

        if is_active:
            self.set_userinfo(request, token_info)
            return None
        else:
            return WebUtils.response_error(error_message="Token不合法", status=status.HTTP_401_UNAUTHORIZED)
