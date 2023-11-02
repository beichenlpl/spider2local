import requests
from ..enums import RequestMethod, ResponseType
from .response import Response


class Request(object):
    __host: str = ''
    __uri: str = ''
    __method: RequestMethod = RequestMethod.GET
    __headers: dict = None
    __params: dict = None
    __data: dict = None
    __files: dict = None
    __timeout: int = 30
    __resp_type: ResponseType = ResponseType.TEXT

    def __init__(self, host: str = '', uri: str = '', method: RequestMethod = RequestMethod.GET, headers: dict = None,
                 data: dict = None, params: dict = None, files: dict = None, timeout: int = 30,
                 resp_type: ResponseType = ResponseType.TEXT):
        self.__host = host
        self.__uri = uri
        self.__method = method
        self.__headers = headers
        self.__params = params
        self.__data = data
        self.__files = files
        self.__timeout = timeout
        self.__resp_type = resp_type

    def set_host(self, host: str):
        self.__host = host

    setHost = set_host

    def set_uri(self, uri: str):
        self.__uri = uri

    setUri = set_uri

    def set_method(self, method: RequestMethod):
        self.__method = method

    setMethod = set_method

    def add_header(self, key: str, value: str):
        if self.__headers is None:
            self.__headers = {}
        self.__headers[key] = value

    addHeader = add_header

    def set_params(self, params: dict):
        self.__params = params

    setParams = set_params

    def set_data(self, data: dict):
        self.__data = data

    setData = set_data

    def set_files(self, files):
        self.__files = files

    setFiles = set_files

    def set_timeout(self, timeout: int):
        self.__timeout = timeout

    setTimeout = set_timeout

    def set_resp_type(self, resp_type: ResponseType):
        self.__resp_type = resp_type

    setRespType = set_resp_type

    def auto_set_cookie(self) -> str:
        if self.__headers is None:
            self.__headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
            }
        self.__headers['Cookie'] = ';'.join(
            [f'{k}={v}' for k, v in requests.get(self.__host, headers=self.__headers).cookies.items()]
        )

        return self.__headers['Cookie']

    autoSetCookie = auto_set_cookie

    def exec(self, resp_encoding: str = 'utf-8') -> Response:
        self.__host = self.__host[0:-1] if self.__host != '' and self.__host[-1:-2:-1] == '/' else self.__host
        self.__uri = self.__uri[1:] if self.__uri != '' and self.__uri[0] == '/' else self.__uri

        response = Response(resp_type=self.__resp_type)
        resp = requests.request(self.__method.value, f'{self.__host}/{self.__uri}', headers=self.__headers,
                                params=self.__params, data=self.__data, files=self.__files, timeout=self.__timeout)

        if response.get_resp_type() == ResponseType.TEXT:
            resp.encoding = resp_encoding
            response.set_content(resp.text)
        elif response.get_resp_type() == ResponseType.JSON:
            resp.encoding = resp_encoding
            response.set_content(resp.json())
        elif response.get_resp_type() == ResponseType.BINARY:
            response.set_content(resp.content)
        else:
            raise RuntimeError('Program execution error!')

        return response
