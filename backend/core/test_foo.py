from core.fields import Animal


def test_speaking():
    Animal().speak() == "bark"
