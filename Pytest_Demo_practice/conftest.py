import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Firefox", "IE") , ("Giri", "Rohit" , "Surya")])
def crossBrowser(request):
    return request.param

