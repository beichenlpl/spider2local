from bs4 import BeautifulSoup

from .entity import Entity
from .response import Response


class FilterRule(object):
    el_name: str = ''
    attrs: dict = None
    is_multiple: bool = False

    def __init__(self, el_name: str, attrs: dict, is_multiple: bool = False):
        self.el_name = el_name
        self.attrs = attrs
        self.is_multiple = is_multiple


class Filter(object):
    __response: Response = None
    __rules: list[FilterRule] = None

    def __init__(self, response: Response = None, rules: list[FilterRule] = None):
        self.__response = response
        self.__rules = rules

    def set_response(self, response: Response):
        self.__response = response

    setResponse = set_response

    def set_rules(self, rules: list[FilterRule]):
        self.__rules = rules

    setRules = set_rules

    def exec(self) -> Entity:
        soup = BeautifulSoup(self.__response.get_content(), 'html.parser')
        entity = Entity()

        first_rule: FilterRule = self.__rules[0]
        node = None
        if first_rule.is_multiple:
            node = soup.find_all(first_rule.el_name, attrs=first_rule.attrs)
            entity.is_multiple = first_rule.is_multiple
            entity.node = node
        else:
            node = soup.find(first_rule.el_name, attrs=first_rule.attrs)
            for rule in self.__rules[1:]:
                node = node.find(rule.el_name, attrs=rule.attrs)
            entity.is_multiple = False
            entity.node = node

        return entity
