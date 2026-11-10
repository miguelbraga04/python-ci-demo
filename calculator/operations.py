def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Nollalla jakaminen ei ole sallittua")

    return a / b

def test_error():
    unused_variable = 10