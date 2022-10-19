import logging
import time

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename='.\\Logs\\automation.log'+time.strftime("%d-%m-%Y"),
        #                     format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger

        logging.basicConfig(
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filename='.\\Logs\\'+'loggen.log' + time.strftime("%d-%m-%Y"),
            level=logging.INFO)
        logger = logging.getLogger()
        return logger




