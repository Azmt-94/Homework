class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        product_dict = {}

        for line in existing_products:
            if line.strip():
                name, weight, category = map(str.strip, line.split(','))
                key = (name, category)
                product_dict[key] = float(weight)

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for product in products:
                key = (product.name, product.category)
                if key in product_dict:
                    product_dict[key] += product.weight
                    print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {product_dict[key]}")
                else:
                    product_dict[key] = product.weight

            for (name, category), weight in product_dict.items():
                file.write(f"{name}, {weight}, {category}\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())


