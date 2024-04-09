import pytest

from Pytest_Demo_practice.conftest import setup


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixturesDemo method")

    def test_firstProgram(self):
        print("Hello")

    def test_SecondProgram(self):
        print("Good Morning")
