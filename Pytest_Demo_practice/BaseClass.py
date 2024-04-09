import inspect
import logging


class BaseClass:
    def test_loggingDemo(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  #fileHandler object

        logger.setLevel(logging.DEBUG)
        return logger

