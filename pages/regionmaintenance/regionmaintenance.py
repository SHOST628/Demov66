from selenium.webdriver.common.by import By

from pages.base.basepage import BasePage


class RegionMaintenance(BasePage):
    """
    区域维护主页面
    """
    _add_criteria_button = (By.XPATH,"")
    _search_button = (By.XPATH,"")
    _new_button = (By.XPATH,"//span[contains(text(),'New')]")
    _exit_button = (By.XPATH,"")
    _enquiry_button = (By.XPATH,"")
    _modify_button = (By.XPATH,"")

    def new(self):
        """
        点击新增按钮
        :return:
        """
        self.click(self._new_button)

    def exit(self):
        """
        点击离开按钮
        :return:
        """
        self.click(self._exit_button)

    def enquiry(self):
        """
        点击查阅按钮
        :return:
        """
        self.click(self._enquiry_button)

    def modify(self):
        """
        点击查阅按钮
        :return:
        """
        self.click(self._modify_button)



