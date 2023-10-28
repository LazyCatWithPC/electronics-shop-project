import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "InstantiateCSVError: Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if __class__.__name__ == 'Item' or __class__.__name__ == 'Phone':
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @staticmethod
    def string_to_number(number: str):
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls, file="items.csv"):
        cls.all.clear()
        try:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError
                else:
                    for row in reader:
                        cls(row["name"], int(row["price"]), int(row["quantity"]))
        except InstantiateCSVError as er:
            print(er.message)
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')


if __name__ == '__main__':
    Item.instantiate_from_csv("items.csv")
    print(Item.all[4].quantity)
