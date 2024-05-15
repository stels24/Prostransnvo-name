
# Функция внутри функции
def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()


def outer_function():

    def inner_function():
        print("Я в области видимости функции test_function")

        inner_function()

    outer_function()