from src.item import Item


class ChangeLang:
    lang = "EN"

    @classmethod
    def change_lang(cls):
        if cls.lang == "RU":
            cls.lang = "EN"
        else:
            cls.lang = "RU"
        return cls.lang


class Keyboard(Item, ChangeLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = self.lang

    @property
    def language(self):
        return self._language

    def change_lang(self):
        super().change_lang()
        self._language = self.lang
        return self
