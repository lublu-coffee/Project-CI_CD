class Calculator:
    @staticmethod
    def summa(a: int, b: int):
        return a + b

    @staticmethod
    def minus(a: int, b: int, reverse: bool = False):
        if reverse:
            a, b = b, a
        return a - b

    @staticmethod
    def multiplication(a: int, b: int):
        return a * b

    @staticmethod
    def division(a: int, b: int, reverse: bool = False):
        if reverse:
            a, b = b, a
        if b == 0:
            return None
        return a / b
