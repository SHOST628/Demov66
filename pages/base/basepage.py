from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import time
import os
import unittest


class BasePage:
    def __init__(self,driver):
        self._driver = driver

    def open(self,url):
        self._open(url)

    def _open(self,url):
        self._driver.get(url)
        self._driver.implicitly_wait(10)

    def click(self,loc):
        self._click(loc)

    def _click(self,loc):
        self.find_element((By.XPATH,loc)).click()

    def double_click(self,loc):
        self._double_click(loc)

    def _double_click(self,loc):
        on_element = self.find_element((By.XPATH,loc))
        ActionChains(self._driver).double_click(on_element).perform()

    def input_text(self,loc,text):
        self._input_text(loc,text)

    def _input_text(self,loc,text):
        element = self.find_element((By.XPATH,loc))
        element.clear()
        element.send_keys(text)

    # def find_element_by_text(self,contain_text):
    #     self._find_element_by_text(contain_text)
    #
    # def _find_element_by_text(self,contain_text,timeout=10,poll_frequency=0.5):
    #     return WebDriverWait(self._driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.XPATH,".//span[contains(text(),'%s')]"%contain_text)))

    def find_element(self,loc):
        element = self._find_element(loc)
        return element

    def _find_element(self,loc,timeout=10,poll_frequency=0.5):
        return WebDriverWait(self._driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.XPATH,loc)))

    def find_elements(self,loc):
        elements = self._find_elements(loc)
        return elements

    def _find_elements(self,loc,timeout=10,poll_frequency=0.5):
        # return WebDriverWait(self._driver,timeout,poll_frequency).until(lambda x:x.find_elements(loc))
        return WebDriverWait(self._driver,timeout,poll_frequency).until(EC.visibility_of_all_elements_located((By.XPATH,loc)))

    def enter(self,loc):
        self._enter(loc)

    def _enter(self,loc):
        self.find_element((By.XPATH,loc)).send_keys(Keys.ENTER)

    def select(self,loc,contain_text):
        self._select(loc,contain_text)

    def _select(self,loc,contain_text):
        """
        choose an option in dropdown list
        loc:the location of drop down list button
        contain_text:contains text in option location
        :param loc:
        :param contain_text:
        :return:
        """
        self.click((By.XPATH,loc))
        option = WebDriverWait(self._driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,".//span[contains(text(),'%s')]"%contain_text)))
        option.click()


    def rselect(self,loc1,loc2):
        self._rselect(loc1,loc2)

    def _rselect(self,loc1,loc2):
        """
        select a random option from a dropdown list
        loc1:the location of drop down list button
        loc2:all option location
        :param loc1:
        :param loc2:
        """
        self.click((By.XPATH,loc1))
        options = self.find_elements((By.XPATH,loc2))
        del options[0]
        option = random.choice(options)
        option.click()

    def save_screenshot(self):
        self._save_screenshot()

    def _save_screenshot(self):
        local_time = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        image_name = local_time + '.png'
        image_dir = os.path.dirname(os.getcwd()) + '/report/screenshot'
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        image_path = image_dir + '/'+ image_name
        self._driver.get_screenshot_as_file(image_path)
        print('lustrat' + image_dir + '/' + image_name + 'luend')

    # @_add
    # def assertIn(self,member,container,msg=None):
    #     assert member in container,msg


# add  checkbox,radiobox

    # capture

    def close(self):
        self._driver.close()

    def quit(self):
        self._driver.quit()

















