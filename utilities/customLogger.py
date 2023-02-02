import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger



# import inspect
# import logging
#
# def customLogger(logLevel):
#     # Gets the name of the class/method from where this method is called
#     loggerName = inspect.stack()[1][3]
#     logger = logging.getLogger(loggerName)
#     # By default, log all messages
#     logger.setLevel(logging.DEBUG)
#
#     fileHandler = logging.Formatter("{0}.log".format(loggerName), mode='w')
#     fileHandler.setLevel(logLevel)
#
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                                   datefmt='%m/%d/%Y %I:%M:%S %p')
#     fileHandler.setFormatter(formatter)
#     logger.addHandler(fileHandler)
#
#     return logger



# And utilize it by below code snippet------------

# import packagename.custom_logger as cl
#
# class LoggingDemo():
#
#     def method1(self):
#         log = cl.customLogger(logging.DEBUG)
#         self.log.debug("debug message")
#         self.log.info("info message")
#         self.log.warn("warn message")
#         self.log.error("error message")
#         self.log.critical("critical message")
