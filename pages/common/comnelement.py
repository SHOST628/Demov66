from selenium.webdriver.common.by import By

class CommonElement:
    """
    维护系统所有页面的公共元素，例如公共的按钮:
    "离开" 、"新增" 、"查阅" 、 "修改" 等等
    """
    _exit_button = (By.XPATH,"")
    _new_button = (By.XPATH,"")
    _enquiry_button =(By.XPATH,"")
    _modify_button = (By.XPATH,"")
    _add_criteria_button = (By.XPATH,"")  #添加搜索条件
    _search_button = (By.XPATH,"")


    def add_criteria(self,option):
        self._add_criteria(option)

    def _add_criteria(self,option):
        """
        添加 "搜索条件"
        option: 要添加的条件
        :param option: str
        :return:
        """
        pass

    def click_search(self):
        self._click_search()

    def _click_search(self):
        """
        点击 "搜索" 按钮
        :return:
        """
        pass

    def click_exit(self):
        self._click_exit()

    def _click_exit(self):
        """
        点击 "离开" 按钮
        :return:
        """
        pass

    def click_new(self):
        self._click_new()

    def _click_new(self):
        """
        点击 "新增" 按钮
        :return:
        """
        pass

    def click_enquiry(self):
        self._click_enquiry()

    def _click_enquiry(self):
        """
        点击 "查阅" 按钮
        :return:
        """
        pass

    def modify(self):
        self._modify()

    def _modify(self):
        """
        点击 "修改" 按钮
        :return:
        """
        pass
