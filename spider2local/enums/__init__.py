from enum import Enum
from enum import unique


@unique
class RequestMethod(Enum):
    """
    请求方法枚举，这里只列举了四种HTTP请求方法。
    Request method enumeration. Only four HTTP request methods are listed here.
    """
    GET: str = 'get'
    POST: str = 'post'
    PUT: str = 'put'
    DELETE: str = 'delete'


@unique
class ResponseType(Enum):
    BINARY: str = 'binary'
    TEXT: str = 'text'
    JSON: str = 'json'
