import logging
import time
import os

# class MyLogger:
#     def __init__(self,logger):
#         # create logger
#         self.logger = logging.getLogger(logger)
#         self.logger.setLevel(logging.DEBUG)
#
#         # create handler to write in a log file
#         rq = time.strftime('%Y%m%d',time.localtime(time.time()))
#         log_path = os.path.dirname(os.getcwd()) + '\logs'
#         log_name = log_path + rq + '.log'
#         fh = logging.FileHandler(log_name)
#         fh.setLevel(logging.DEBUG)
#
#         # create a handler to output to console
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.INFO)
#
#         # define format for outputing
#         formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         # add handler to logger
#         self.logger.addHandler(fh)
#         self.logger.addHandler(ch)
#
#     def getlog(self):
#         return self.logger


# logger = MyLogger('MyLogger').getlog()
# logger.info('print info')
# logger.debug('print debug')
# logger.critical('print critical')


class MyLogger:
    def __init__(self,logger):
        # create logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # create filehandler to write in a file
        strftime = time.strftime('%Y%m%d',time.localtime())
        path = strftime + '.log'
        fh = logging.FileHandler(path)
        fh.setLevel(logging.DEBUG)

        # create StreamHandler to output to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # define formatter to handler
        formmater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formmater)
        ch.setFormatter(formmater)

        # add handler to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger

logger = MyLogger('MyLogger').getLog()

def division():
    try:
        a = 3 / 0
    except Exception as e:
        return e
logger.debug('print debug')
logger.info('print info')
logger.critical('print critical')
logger.warning('print warning')
logger.error('print error')
logger.error(division())





