#module_7_1.py

from pprint import pprint

class Product:
    def __init__(self, name, weight,  category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop(Product):
    def __init__(self, name, weight,  category,  __file_name = 'products.txt'):
        super().__init__(name, weight,  category)
        self.__file_name = __file_name

    def get_products(self):
        product_file = open(self.__file_name, 'r')
        pf = product_file.read()
        product_file.close()
        return f'{pf}'

    def add(self, *products):
        try:  # Проверка на наличие файла
            f = open(self.__file_name)
            f.close()
        except FileNotFoundError:
            open(self.__file_name, 'a')
        for i in products:
            a = (str(i))  # продукт для проверки
            product_file = open(self.__file_name, 'r')
            file_list = product_file.read()
            product_file.close()
            if a in file_list:  # есть ли продукт в файле
                print(f'Продукт {a} уже есть в магазине')
            else:
                product_file = open(self.__file_name, 'a')  # открывает для обновления
                product_file.write(f'{a}\n')  # Переписывает с переносом строки
                product_file.close()  # Закрывает'''

s1 = Shop(None, 0, None)
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

