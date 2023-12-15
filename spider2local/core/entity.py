from bs4 import BeautifulSoup, PageElement, Tag


class Entity(object):
    def __init__(self):
        self.node: BeautifulSoup | PageElement | Tag = None
        self.is_multiple: bool = False

    def text(self) -> str | list[str]:
        if self.is_multiple:
            texts = []
            for item in self.node:
                texts.append(item.text)
            return texts

        return self.node.text

    def attr(self, name: str) -> str | list[str]:
        return self.node.attrs[name]

    def attrs(self, names: list[str]) -> list[str]:
        attrs: list[str] = []
        for item, name in zip(self.node, names):
            attrs.append(item[name])
        return attrs
