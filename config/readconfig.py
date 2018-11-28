import os
from configparser import ConfigParser

config_path = os.path.dirname(os.getcwd()) + "/config/config.ini"
config = ConfigParser()
config.read(config_path,encoding='utf-8')
url = config.get('URL','url')
report_path = config.get('Report','Path')
db_url = config.get('DataSource','DB')
browser_name = config.get("BrowserType","BrowserName")
login_user = config.get("Login","User")
login_password = config.get("Login","Psw")
debug_mode = int(config.get("Debug","Mode"))
execute_user = config.get("Debug", "Execute_User")
CaseMixed = config.get("CaseMixed","CaseMixed")

# email config
if_send = config.get("Mail","If_Send")
email_host = config.get("Mail","Host")
email_user = config.get("Mail","User")
email_psw = config.get("Mail","Psw")
to_addrs = config.get("Mail","To_Addrs")





