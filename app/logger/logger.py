import logging


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("LBroker.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def debug(self, *args):
        msg = ';'.join('%s' % arg for arg in args)
        self.logger.debug(msg)

    def warning(self, *args):
        msg = ';'.join('%s' % arg for arg in args)
        self.logger.warning(msg)

    def error(self, *args):
        msg = ';'.join('%s' % arg for arg in args)
        self.logger.error(msg)


l_log = Logger()
