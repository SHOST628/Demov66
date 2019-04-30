from config import readconfig
from pages.keywords.keyword import BaseKeyword
from common.logger import logger
from selenium.webdriver.common.keys import Keys
from common.oracle import Oracle
import requests

class LoginPage(BaseKeyword):
    _username_locationid = "//*[@id='xf_staffcode']/input"
    _password_locationid = "//*[@id='xf_password']"
    _submit_locationid = "//*[@id='okbtn']/span/span"
    _language_button_locationid = "//*[@id='languagetype']/input"
    _title_loc = "//div[@class='v-slot v-slot-v-appheader']/div/div/div[3]/div"
    # _prompt_loc = "//div[@class='v-Notification error v-Notification-error']"

    def input_text(self,loc,text,index = None):
        """
        it can choose a absolutely location path or a relative location path
        :param loc:
        :param text:
        :param index:
        :return:
        """
        if index:
            elements = self.find_elements(loc)
            index = int(index)
            element = elements[index]
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
        else:
            element = self.find_element(loc)
            element.clear()
            element.send_keys(text)

    def get_location(self,location_id):
        oracle = Oracle(readconfig.db_url)
        sql = "select xf_location from xf_pagelocation where xf_locationid = '%s'" % location_id
        location_list = oracle.dict_fetchall(sql)
        location = location_list[0]['XF_LOCATION']
        if location is None:
            raise Exception("location_id 错误，无法找到对应的location")
        return location

    def open_backend(self):
        self.open(readconfig.url)

    def input_user(self,text):
        self.input_text(self._username_locationid, text)
        self.enter(self._username_locationid)

    def input_password(self,text):
        self.input_text(self._password_locationid, text)

    def choose_language(self,text):
        self.select(self._language_button_locationid, text)

    def click_submit(self):
        self.click(self._submit_locationid)

    def login(self,user,psw):
        self.open_backend()
        try:
            self.input_user(user)
            logger.info("登录用户 %s"% user)
            self.input_password(psw)
            logger.info("登录密码 %s"% psw)
            self.click_submit()
        except Exception as e:
            logger.exception(e)
            raise e

















