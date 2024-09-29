import os

from datetime import datetime

from logging.handlers import BaseRotatingHandler


class DateRotatingHandler(BaseRotatingHandler):
    def __init__(self, filename: str):
        self.base_filename = os.path.basename(filename)
        self.base_dir = os.path.dirname(filename)
        BaseRotatingHandler.__init__(self, self.create_file_name(), 'a')

    def create_file_name(self, default_name: str = None):
        return f'{self.base_dir}/{datetime.now().date()}_{self.base_filename}'

    def _open(self):
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
        return open(self.create_file_name(), self.mode, encoding=self.encoding, errors=self.errors)

    def shouldRollover(self, record):
        if os.path.exists(self.baseFilename) and not os.path.isfile(self.baseFilename):
            return False
        searched_file = self.create_file_name()
        if not os.path.exists(searched_file):
            return True
        return False

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        self.stream = self._open()
