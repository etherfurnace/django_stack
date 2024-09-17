import traceback

from django.apps import apps
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from loguru import logger
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.components.base import DEBUG

urlpatterns = [

    # path('', RedirectView.as_view(url='/admin')),

    # rest_framework_simplejwt自带的得到token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # 刷新JWT
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # 验证token
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    # 将token加入黑名单
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("admin/", admin.site.urls),
]

if DEBUG:
    import debug_toolbar
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="API",
            default_version="v1",
            description="description",
            terms_of_service="",
            contact=openapi.Contact(email=""),
            license=openapi.License(name=""),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path(
            "swagger<format>/",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
        path("__debug__/", include(debug_toolbar.urls)),
    ]

for app_config in apps.get_app_configs():
    app_name = app_config.name
    try:
        # app_name是apps.开头的，就import这个app的urls.py
        if app_name.startswith("apps."):
            logger.debug(f"加载[{app_name}]的路由......")
            urls_module = __import__(f"{app_name}.urls", fromlist=["urlpatterns"])
            urlpatterns.append(path("", include(urls_module)))

    except ImportError:
        traceback.print_exc()
