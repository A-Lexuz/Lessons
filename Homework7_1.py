class Product:
    def __init__(self, name, weigh, category):
        self.name = name
        self.weigh = float(weigh)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigh}, {self.category}'


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        added_products = file.read()
        file.close()
        return added_products
    def add(self, *products):
        for i in products:
            if i.name in self.get_products():
                file = open(self.__file_name, 'a')
                print(f'Продукт {i.name} уже есть в магазине.')
                file.close()
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i} \n')
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
