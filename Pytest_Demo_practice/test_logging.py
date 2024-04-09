# Logging is in-build features in python . We need to create object , with the object we have log.
# To catch a filename in the log use __name__ in get logger arguments.
# To print the log reports in the file use addHandler method .
# In addHandler we have to pass fileHandler object.
# fileHandler is nothing but the location of the file and , It comes from parent logging method.
# In format -- % is used in format because it will pull output at run time . s is used to convert it in string .
import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)  #fileHandler object
    logger.setLevel(logging.ERROR)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical Issue")




