from .enums import *
from .core.entity import Entity
from .core.filter import Filter
from .core.request import Request
from .core.response import Response
from .core.filter import FilterRule


def send_request(req: Request, resp_encoding: str = 'utf-8') -> Response:
    return req.exec(resp_encoding)


sendRequest = send_request


def resp_filter(flt: Filter) -> Entity:
    return flt.exec()


respFilter = resp_filter
