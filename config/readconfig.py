import os
from configparser import ConfigParser

class Rconfig:
    def __init__(self):
        self.config_path = os.path.dirname(os.getcwd()) + "/config/config.ini"

config = ConfigParser()
Rconfig = Rconfig()
config.read(Rconfig.config_path,encoding='utf-8')
url = config.get('URL','url')
report_path = config.get('Report','Path')
db_url = config.get('DataSource','DB')
browser_name = config.get("BrowserType","BrowserName")




