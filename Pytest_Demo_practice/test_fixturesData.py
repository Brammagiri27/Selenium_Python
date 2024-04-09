import pytest

from Pytest_Demo_practice.BaseClass import BaseClass


# When you returning data from fixture to the method , we have to add arguments in the method .
# data has been returning by using index also .
@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_edit_profile(self,dataLoad):
        log = self.test_loggingDemo()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        # print(dataLoad)
        # print(dataLoad[1])
        # print(dataLoad[2])

