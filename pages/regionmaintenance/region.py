from selenium.webdriver.common.by import By
from pages.base.basepage import BasePage
from pages.navigation import systemmenu

class Region(BasePage):
    """
    区域维护明细页面
    """
    _exit = (By.XPATH,"//div[@class='v-expand']/div[4]/div/span[1]/span")
    _clear = (By.XPATH,"")
    _region_code = (By.XPATH,"//*[@id='XF_REGIONCODE']")
    _name = (By.XPATH,"//*[@id='XF_NAME']")
    _country = (By.XPATH,"//*[@id='XF_COUNTRY']")
    _description = (By.XPATH,"//*[@id='XF_DESCI']")
    _local_currency = (By.XPATH,"//*[@id='XF_BASECURRCODE']/div")
    _random_option = (By.XPATH,"//div[@class='v-filterselect-suggestmenu']/table/tbody//span")
    _sales_price_include_tax = (By.XPATH,"//*[@id='XF_PRICEINCLUDETAX']/div")
    _language = (By.XPATH,"")
    _date_format = (By.XPATH,"")
    _date_time_format = (By.XPATH,"")
    _yes_button = (By.XPATH,"//span[contains(text(),'Yes')]")
    _no_button = (By.XPATH,"//span[contains(text(),'No')]")

    def navigate_region_maintenance(self):
        """
        导航到区域维护页面
        :return:
        """
        self.click(systemmenu.system_menu)
        self.click(systemmenu.system_configuration)
        self.click(systemmenu.backend_system_configuration)
        self.click(systemmenu.region_maintanence)

    def click_exit(self):
        """
        点击"离开" 按钮
        :return:
        """
        self.click(self._exit)

    def click_clear(self):
        """
        点击"清除" 按钮
        :return:
        """
        self.click(self._clear)

    def input_region_code(self,text):
        """
        输入“区域编码”

        :param text:str
        :return:
        """
        self.input_text(self._region_code,text)

    def input_name(self,text):
        """
        输入 "名称"
        :param text:str
        :return:
        """
        self.input_text(self._name,text)

    def input_country(self,text):
        """
        输入 "所属国家"
        :param text:str
        :return:
        """
        self.input_text(self._country,text)

    def input_description(self,text):
        """
        输入 "描述"
        :param text:str
        :return:
        """
        self.input_text(self._description,text)

    def select_local_currency(self,contain_text):
        """
        选择 "本位币"
        contain_text:本位币下拉里面选择包含的文字，最好是选项完整的信息，否则可能定位不到
        :param contain_text:str
        :return:
        """
        self.select(self._local_currency,contain_text)

    def select_sales_price_include_tax(self):
        """
        选择 "销售价格是否含税"
        :return:
        """
        # 随机选择下拉选项
        self.rselect(self._sales_price_include_tax,self._random_option)

    def select_language(self):
        """
        选择 "语言"
        :return:
        """
        # 随机选择下拉选项
        self.rselect(self._language,self._random_option)

    def click_yes(self):
        """
        点击离开按钮时，页面弹出弹框，选择Yes
        :return:
        """
        self.click(self._yes_button)

    def click_no(self):
        """
        点击离开按钮时，页面弹出弹框，选择No
        :return:
        """
        self.click(self._no_button)

    # def hide(self):
    #     """
    #     隐藏页面弹框
    #     :return:
    #     """
    #     self._driver.execute_script('document.getElementByclassName("v-Notification error v-Notification-error").style.display="none";')







