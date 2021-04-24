"""
7.	Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку 
методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса 
(комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного 
результата.
"""


class Complex:
    def __init__(self, a: float, b: float):
        """
        Complex number class.
        :param a: real part
        :param b: imaginary part
        """
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}{"+" if self.b > 0 else "-"}{abs(self.b)}i'

    # Сложение
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    # Сложение +=
    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b
        return self

    # Вычитание
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    # Вычитание -=
    def __isub__(self, other):
        self.a -= other.a
        self.b -= other.b
        return self

    # Умножение
    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b,
                       self.a * other.b + self.b * other.a)

    # Умножение *=
    def __imul__(self, other):
        self.a = self.a * other.a - self.b * other.b
        self.b = self.a * other.b + self.b * other.a
        return self

    # Деление
    def __truediv__(self, other):
        return Complex((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2),
                       (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2))

    # Деление /=
    def __itruediv__(self, other):
        self.a = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
        self.b = (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)
        return self


one = Complex(10, 5)
two = Complex(2, 3)
print(one, two)
print(f"Сложение: {one + two}")
print(f"Вычитание: {one - two}")
print(f"Умножение: {one * two}")
print(f"Деление: {one / two}")
one += two
print(one)
