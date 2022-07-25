from configparser import ConfigParser
import os


class Config:
    def __init__(self, filename=None, section='postgresql'):
        if filename is None:
            filename = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'database.ini')
            print(filename)
