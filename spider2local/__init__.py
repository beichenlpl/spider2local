from .local_enums import *
from .core import Entity
from .core import Filter, AttributeFilter, AttributeFilterRule
from .core import Request
from .core import Response


def send_request(req: Request, resp_encoding: str = 'utf-8') -> Response:
    return req.exec(resp_encoding)


sendRequest = send_request


def resp_filter(flt: Filter) -> Entity:
    return flt.exec()


respFilter = resp_filter
