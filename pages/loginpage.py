from selenium.webdriver.common.by import By
from config import readconfig
from pages.base.keyword import Action
import unittest
from common.logger import logger

class LoginPage(Action):
    _username_loc = "//*[@id='xf_staffcode']/input"
    _password_loc = "//*[@id='xf_password']"
    _submit_loc = "//*[@id='okbtn']/span/span"
    _language_button_loc ="//div[@id='languagetype']"
    _title_loc = "//div[@class='v-slot v-slot-v-appheader']/div/div/div[3]/div"
    # _prompt_loc = "//div[@class='v-Notification error v-Notification-error']"

    def open_backend(self):
        self.open(readconfig.url)

    def input_user(self,text):
        self.input_text(self._username_loc,text)
        self.enter(self._username_loc)

    def input_password(self,text):
        self.input_text(self._password_loc,text)

    def choose_language(self,text):
        self.select(self._language_button_loc,text)

    def click_submit(self):
        self.click(self._submit_loc)

    def login(self,user,psw):
        try:
            self.open_backend()
        except:
            logger.error("无法访问该路径 %s"% readconfig.url)
        try:
            self.input_user(user)
            logger.info("登录用户 %s"% user)
            self.input_password(psw)
            logger.info("登录密码 %s"% psw)
            # self.choose_language("简体中文 ( zh_CN )")
            self.click_submit()
        except Exception as e:
            logger.exception(e)
            raise e

    def _get_title(self):
        return self.find_element(self._title_loc).text

    def if_login_success(self):
        caption = "科传股份espos系统"
        # caption = self._get_title()
        unittest.TestCase().assertIn("test",caption,"login fail")
        # self.assertIn("科传股份",caption,"login fail")


















