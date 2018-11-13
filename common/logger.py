import logging
from logging import handlers
import os
from common.file import mkdir

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self, filename, filelevel='debug', streamlevel='info', when='D', backupCount=10, fformatter='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', sformatter='%(message)s'):
        self.folder = os.path.dirname(os.getcwd()) + '\logs'
        self.filename = os.path.join(self.folder, filename)
        # set logger format
        self.file_formatter = logging.Formatter(fformatter)
        self.stream_formatter = logging.Formatter(sformatter)
        self.filelevel = filelevel
        self.streamlevel = streamlevel
        self.when = when
        self.backupcount = backupCount

    def get_logger(self):
        mkdir(self.folder)
        self.logger = logging.getLogger(self.filename)
        self.logger.setLevel(self.level_relations.get(self.filelevel))  # set logger level
        sh = logging.StreamHandler()
        sh.setLevel(self.level_relations.get(self.streamlevel))
        sh.setFormatter(self.stream_formatter)
        th = handlers.TimedRotatingFileHandler(filename=self.filename, when=self.when, backupCount=self.backupcount, encoding='utf-8')  # separate file by time
        th.setFormatter(self.file_formatter)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)
        return self.logger

logger = Logger(filename='case').get_logger()

