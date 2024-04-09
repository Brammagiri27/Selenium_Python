# Any pytest file should be start with test_
# Every testcase(or)code will be declared under functions/Methods .
# pytest method names should start with test
# Method name should be in meaning full related to your project .
# In Pytest every method is treated as 1 testcase .
# Cmtline terminal -- To run all testcases py.test command were used .
# py.test -v -s commands for details & console output .
# -v stand for verbo's -- it gives detail descriptions.
# -s is flag used to console the output in cmtline
# -k stands for regular Expressions.Ex :If you want to run only the method names like Creditcard use (py.test -k Creditcard -v -s ).
#-m stands for mark (tags) @pytest.mark.smoke.
# @pytest.mark.skip is used to skip the specific testcase.
# @pytest.mark.xfail - It will run , but reports not displayed in console .
# fixtures are used as setup and tear down methods for all test cases .
# Conftest file is to generalize fixture and make it available to all testcases.
# In fixtures , if you put scope to class level , it is executed once to the class level alone
# or else it defaultly executed to the method level.
# fixtures is not only run pre-request , it also helps to load data .



def test_fixtureDemo():
    print("i will execute steps in fixturesDemo method")


def test_firstProgram(crossBrowser):
    print(crossBrowser[2],crossBrowser[1])






