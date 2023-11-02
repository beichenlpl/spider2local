from typing import Any
from ..enums import ResponseType


class Response(object):
    __resp_type: ResponseType = ResponseType.TEXT
    __content: Any = None

    def __init__(self, resp_type: ResponseType = ResponseType.TEXT, content: Any = None):
        self.__resp_type = resp_type
        self.__content = content

    def set_resp_type(self, resp_type):
        self.__resp_type = resp_type

    setRespType = set_resp_type

    def set_content(self, content: Any):
        self.__content = content

    setContent = set_content

    def get_resp_type(self):
        return self.__resp_type

    getRespType = get_resp_type

    def get_content(self):
        return self.__content

    getContent = get_content
