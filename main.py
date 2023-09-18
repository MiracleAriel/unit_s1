# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from math import sqrt
from datetime import datetime
# Задача 0


def square_root(num: float) -> float:
    if num < 0:
        raise RuntimeError(f"Число {num} должно быть неотрицательным")
    return sqrt(num)


def test_square_root_positive():
    assert square_root(25) == 5, "Тест с положительными числами провален"


def test_square_root_zero():
    assert square_root(0) == 0, "Тест с нулевыми значениеями провален"


def test_square_root_negative():
    try:
        square_root(-5)
    except RuntimeError:
        print("Все тесты прошли")


# Задача 4
def happy_NY():
    current_date = datetime.now()
    assert current_date > datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0), "2024 еще не наступил"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()

    happy_NY()


# task 1
import unittest

class Calculator:

    def calculateDiscount(self, purchase_amount, discount_percentage):
        if purchase_amount <= 0:
            raise ArithmeticError("Purchase amount cannot be zero or negative")
        if discount_percentage < 0:
            raise ArithmeticError("Discount percentage cannot be negative")
        
        discount = (purchase_amount * discount_percentage) / 100
        discounted_price = purchase_amount - discount
        return discounted_price

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculateDiscount_ValidInput_ReturnsDiscountedPrice(self):
        purchase_amount = 100.0
        discount_percentage = 10.0
        expected_discounted_price = 90.0

        discounted_price = self.calculator.calculateDiscount(purchase_amount, discount_percentage)
        self.assertEqual(discounted_price, expected_discounted_price)

    def test_calculateDiscount_ZeroPurchaseAmount_ThrowsArithmeticException(self):
        purchase_amount = 0.0
        discount_percentage = 10.0

        with self.assertRaises(ArithmeticError):
            self.calculator.calculateDiscount(purchase_amount, discount_percentage)

    def test_calculateDiscount_NegativePurchaseAmount_ThrowsArithmeticException(self):
        purchase_amount = -100.0
        discount_percentage = 10.0

        with self.assertRaises(ArithmeticError):
            self.calculator.calculateDiscount(purchase_amount, discount_percentage)

    def test_calculateDiscount_NegativeDiscountPercentage_ThrowsArithmeticException(self):
        purchase_amount = 100.0
        discount_percentage = -10.0

        with self.assertRaises(ArithmeticError):
            self.calculator.calculateDiscount(purchase_amount, discount_percentage)

if __name__ == '__main__':
    unittest.main()

# task 2

import unittest

class Product:

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Shop:

    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def sortProductsByPrice(self):
        self.products.sort(key=lambda x: x.price)

    def getMostExpensiveProduct(self):
        if not self.products:
            return None
        return max(self.products, key=lambda x: x.price)

class TestShop(unittest.TestCase):

    def setUp(self):
        self.shop = Shop()

    def test_sortProductsByPrice_SortsProductsByPriceAscending(self):
        product1 = Product("Product 1", "Description 1", 10.0)
        product2 = Product("Product 2", "Description 2", 5.0)
        product3 = Product("Product 3", "Description 3", 20.0)

        self.shop.addProduct(product1)
        self.shop.addProduct(product2)
        self.shop.addProduct(product3)

        expected_sorted_products = [product2, product1, product3]

        self.shop.sortProductsByPrice()
        self.assertEqual(self.shop.products, expected_sorted_products)

    def test_getMostExpensiveProduct_ReturnsMostExpensiveProduct(self):
        product1 = Product("Product 1", "Description 1", 10.0)
        product2 = Product("Product 2", "Description 2", 5.0)
        product3 = Product("Product 3", "Description 3", 20.0)

        self.shop.addProduct(product1)
        self.shop.addProduct(product2)
        self.shop.addProduct(product3)

        most_expensive_product = self.shop.getMostExpensiveProduct()
        self.assertEqual(most_expensive_product, product3)

if __name__ == '__main__':
    unittest.main()
