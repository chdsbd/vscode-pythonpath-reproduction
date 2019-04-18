from core.foo import Animal


def test_speaking():
    Animal().speak() == "bark"
