from typing import Any
from ..local_enums import ResponseType


class Response(object):
    def __init__(self, resp_type: ResponseType = ResponseType.TEXT, headers: Any = None, content: Any = None):
        self.__resp_type = resp_type
        self.__headers = headers
        self.__content = content

    def set_resp_type(self, resp_type: ResponseType):
        self.__resp_type = resp_type

    setRespType = set_resp_type

    def set_headers(self, headers: Any):
        self.__headers = headers

    setHeaders = set_headers

    def set_content(self, content: Any):
        self.__content = content

    setContent = set_content

    def get_resp_type(self):
        return self.__resp_type

    getRespType = get_resp_type

    def get_headers(self):
        return self.__headers

    getHeaders = get_headers

    def get_content(self):
        return self.__content

    getContent = get_content
