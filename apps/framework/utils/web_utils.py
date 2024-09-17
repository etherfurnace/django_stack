import mimetypes
import os
import urllib

from django.http import JsonResponse, FileResponse
from rest_framework import status


class WebUtils:
    @staticmethod
    def response_success(response_data={}, meta={}):
        return JsonResponse(
            {"meta": meta, "data": response_data, "result": True, "message": ""},
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def response_error(response_data={}, error_message="", status=status.HTTP_400_BAD_REQUEST):
        return JsonResponse(
            {"data": response_data, "result": False, "message": error_message},
            status=status,
        )

    @staticmethod
    def download_local_file(local_path, file_name):
        """下载本地文件"""

        # 使用 mimetypes 模块来获取文件的 MIME 类型
        content_type, _ = mimetypes.guess_type(file_name)

        # 默认 MIME 类型
        if content_type is None:
            content_type = "application/octet-stream"

        # 构建文件路径
        file_path = os.path.join(local_path, file_name)

        # 构建响应对象并设置文件名和类型
        response = FileResponse(open(file_path, "rb"), content_type=content_type)

        # 文件名进行URL编码
        encoded_file_name = urllib.parse.quote(file_name)
        response["Content-Disposition"] = f'attachment; filename="{encoded_file_name}"'

        return response
