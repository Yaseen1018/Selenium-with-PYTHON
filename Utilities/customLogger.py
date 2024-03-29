import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\"+"automation.log",
                        format = '%(asctime)s: %(levelname)s: %(message)s', datefmt = '%m%d%Y %Y:%M%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
