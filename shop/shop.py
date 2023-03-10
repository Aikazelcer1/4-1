import csv
import os.path

from shop.errors import InstantiateCSVError


class Item:
    pay_rate = 0.85
    all = []
    path_to_csv = os.path.join('items.csv')

    def __init__(self, name, price, quantity):
        self.__name = name
        if price < 0 or quantity < 0:
            raise AttributeError('Цена и количество товара не могут быть меньше 0')
        else:
            self.__price = price
            self.__quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return f'Item(name={self.__name}, price={self.__price}, quantity={self.__quantity})'

    def __str__(self) -> str:
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError('Правый операнд должен быть объектом класса Item или объектом наследника класса Item')
        return self.__quantity + other.__quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        price = round(price, 2)
        self.__price = price

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    def calculate_total_price(self):
        total_cost = self.__price * self.__quantity
        return total_cost

    def apply_discount(self):
        self.price = round(self.price * self.pay_rate, 2)
        return self.price

    @staticmethod
    def get_price(num: str):
        if '.' in num:
            if num.split('.')[1] == '0':
                return int(num.split('.')[0])
            return float(num)
        return int(num)

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        try:
            with open(path, 'r') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    if len(row.keys()) > 3 or list(row.keys()) != ['name', 'price', 'quantity']:
                        raise InstantiateCSVError(message='InstantiateCSVError: Файл item.csv поврежден')
                    cls(name=row['name'], price=cls.get_price(row['price']), quantity=int(row['quantity']))
        except FileNotFoundError:
            print(f'FileNotFoundError: Отсутствует файл {path}')
        except InstantiateCSVError as error:
            print(error.message)


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim not in [1, 2]:
            raise AttributeError('Количество физических SIM-карт должно быть равно 1 или 2.')
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'Phone').replace(')', f', number_of_sim={self.__number_of_sim})')

    @property
    def number_of_sim(self) -> int:

        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:

        if number_of_sim in [1, 2]:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть равно 1 или 2.')


class MixinKeyboardLayout:

    def __init__(self, *args, **kwargs):
        self.__language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self):

        return self.__language

    def change_lang(self):

        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(MixinKeyboardLayout, Item):

    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'KeyBoard')