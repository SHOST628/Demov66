import os
from configparser import ConfigParser

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
config_path = os.path.dirname(os.getcwd()) + "/config/config.ini"
config = ConfigParser()
config.read(config_path,encoding='utf-8-sig')
browser_name = config.get("BrowserType","BrowserName")
report_path = config.get('Report','Path')

# DB config
database_connection_url = config.get('DataSource', 'DatabaseConnectionUrl')
database_user = config.get('DataSource', 'DatabaseUser')
database_password = config.get('DataSource', 'DatabasePassword')
db_url = database_user + '/' + database_password + '@' + database_connection_url

# backend login config
url = config.get("Backend","Url")
login_user = config.get("Backend","User")
login_password = config.get("Backend","Psw")

debug_mode = int(config.get("Debug","Mode"))
execute_user = config.get("Debug", "Execute_User")
CaseMixed = config.get("CaseMixed","CaseMixed")

# email config
if_send = config.get("Mail","If_Send")
email_host = config.get("Mail","Host")
email_user = config.get("Mail","User")
email_psw = config.get("Mail","Psw")
Receivers = config.get("Mail", "Receivers")





