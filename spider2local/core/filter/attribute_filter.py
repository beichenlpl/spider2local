from bs4 import BeautifulSoup

from spider2local.core.entity import Entity
from spider2local.core.response import Response
from .filter import Filter


class AttributeFilterRule(object):
    def __init__(self, el_name: str, attrs: dict, is_multiple: bool = False):
        self.el_name = el_name
        self.attrs = attrs
        self.is_multiple = is_multiple


class AttributeFilter(Filter):
    def __init__(self, response: Response = None, rules: list[AttributeFilterRule] = None):
        super().__init__()
        self.__response = response
        self.__rules = rules

    def set_response(self, response: Response):
        self.__response = response

    setResponse = set_response

    def set_rules(self, rules: list[AttributeFilterRule]):
        self.__rules = rules

    setRules = set_rules

    def exec(self) -> Entity:
        soup = BeautifulSoup(self.__response.get_content(), 'html.parser')
        entity = Entity()

        first_rule: AttributeFilterRule = self.__rules[0]
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
