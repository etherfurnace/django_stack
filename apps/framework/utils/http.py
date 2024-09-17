import json
import traceback

import requests
from django.utils.translation import gettext_lazy as _
from loguru import logger


class HttpClient:
    def __init__(self):
        self.session = requests.session()
        self.headers = {"Content-Type": "application/json; charset=utf-8"}

    def get(self, url, params=None, timeout=None, **kwargs):
        """
        发送 GET 请求
        """
        try:
            response = self.session.request(method="GET", url=url, params=params, timeout=timeout, **kwargs)
            return self.handle_response(response, url, "GET", params)
        except requests.exceptions.Timeout:
            self.handle_timeout(url, "GET", params, timeout)

    def post(self, url, params=None, timeout=None, **kwargs):
        """
        发送 POST 请求
        """
        try:
            self.session.headers.update(self.headers)
            response = self.session.request(method="POST", url=url, data=json.dumps(params), timeout=timeout, **kwargs)
            return self.handle_response(response, url, "POST", params)
        except requests.exceptions.Timeout:
            self.handle_timeout(url, "POST", params, timeout)

    def put(self, url, params=None, timeout=None, **kwargs):
        """
        发送 PUT 请求
        """
        try:
            self.session.headers.update(self.headers)
            response = self.session.request(method="PUT", url=url, data=json.dumps(params), timeout=timeout, **kwargs)
            return self.handle_response(response, url, "PUT", params)
        except requests.exceptions.Timeout:
            self.handle_timeout(url, "PUT", params, timeout)

    def delete(self, url, params=None, timeout=None, **kwargs):
        """
        发送 DELETE 请求
        """
        try:
            response = self.session.request(method="DELETE", url=url, params=params, timeout=timeout, **kwargs)
            return self.handle_response(response, url, "DELETE", params)
        except requests.exceptions.Timeout:
            self.handle_timeout(url, "DELETE", params, timeout)

    def handle_response(self, response, url, method, params):
        """
        处理响应结果
        """
        logger.debug("请求记录, url={}, method={}, params={}, response={}".format(url, method, params, response))

        if response.status_code != requests.codes.ok:
            err_msg = _("返回异常状态码，status_code=%s，url=%s，method=%s，params=%s") % (
                response.status_code,
                url,
                method,
                json.dumps(params),
            )
            raise Exception(err_msg)

        try:
            return response.json()
        except Exception:
            err_msg = _("返回内容不符合 JSON 格式，url=%s，method=%s，params=%s，error=%s，response=%s") % (
                url,
                method,
                json.dumps(params),
                traceback.format_exc(),
                response.text[:1000],
            )
            raise Exception(err_msg)

    def handle_timeout(self, url, method, params, timeout):
        """
        处理请求超时情况
        """
        err_msg = _("请求超时，url=%s，method=%s，params=%s，timeout=%s") % (
            url,
            method,
            params,
            timeout,
        )
        raise Exception(err_msg)
