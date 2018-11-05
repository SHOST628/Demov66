from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import time
import os
import re
from common.storage import Storage
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from unittest import TestCase

class Action:
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
        self.find_element(loc).click()

    def double_click(self,loc):
        self._double_click(loc)

    def _double_click(self,loc):
        on_element = self.find_element(loc)
        ActionChains(self._driver).double_click(on_element).perform()

    def input_text_by_index(self,loc,index,text):
        elements = self.find_elements(loc)
        element = elements[index]
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def input_text(self,loc,text):
        self._input_text(loc,text)

    def _input_text(self,loc,text):
        element = self.find_element(loc)
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

    def _find_element(self,loc,timeout=15,poll_frequency=0.5):
        try:
            return WebDriverWait(self._driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.XPATH,loc)))
            # return WebDriverWait(self._driver,timeout,poll_frequency).until(EC.presence_of_element_located((By.XPATH,loc)))
        except WebDriverException as e:
            raise e

    def find_elements(self,loc):
        elements = self._find_elements(loc)
        return elements

    def _find_elements(self,loc,timeout=15,poll_frequency=0.5):
        try:
            # return WebDriverWait(self._driver,timeout,poll_frequency).until(lambda x:x.find_elements(loc))
            return WebDriverWait(self._driver,timeout,poll_frequency).until(EC.visibility_of_all_elements_located((By.XPATH,loc)))
        except NoSuchElementException as e:
            raise e
        except WebDriverException as e:
            raise e

    def enter(self,loc):
        self._enter(loc)

    def _enter(self,loc):
        self.find_element(loc).send_keys(Keys.ENTER)

    def tab(self,loc):
        self.find_element(loc).send_keys(Keys.TAB)

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
        # self.click((loc))
        # target = WebDriverWait(self._driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,".//span[contains(text(),'%s')]"%contain_text)))
        # auto scroll into the target
        # self._driver.execute_script("arguments[0].scrollIntoView(true);",target)
        # target.click()

        # action = ActionChains(self._driver)
        # action.move_to_element(target)
        # action.click().perform()

        self.input_text(loc,contain_text)
        # target = WebDriverWait(self._driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,".//span[contains(text(),'%s')]"%contain_text)))
        # target.click()
        self.enter(loc)

        # self.input_text(loc,contain_text)
        # self.enter(loc)

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
        self.click(loc1)
        targets = self.find_elements(loc2)
        del targets[0]
        option = random.choice(targets)
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

    #get element text
    def _get_text(self,loc):
        text = self.find_element(loc).text
        return text

    def assertIn(self,member, loc, msg=None):
        text = self._get_text(loc)
        assert member in text,'%s'%msg

    # add  checkbox,radiobox

    # store variate
    def storage_docno(self,var):
        loc = "//div[@class='popupContent']/div/p"
        contain_text = self.find_element(loc).text
        # get documnent no
        doc_no =''.join(re.findall("[A-Za-z0-9]",contain_text))
        # variate name
        setattr(Storage,var,doc_no)

    def locate_record(self,var):
        # self._storage_docno(var)
        docno = getattr(Storage,var)
        loc = "//div[text()='%s']"%docno
        self.click(loc)

    def click_by_index(self,loc,index):
        """
        you can choose this keyword to locate element when a page without an only id contains many same properties in a page
        :param loc:
        :param index: choose a correct index starting with 0
        :return:
        """
        i = int(index)
        elements = self.find_elements(loc)
        elements[i].click()

    def accept_prompt(self):
        # this is all prompt location in v66
        loc = "//div[@class='popupContent']/div/p"
        # loc = ""
        self.click(loc)

    # def sleep(self,seconds):
    #     time.sleep(seconds)

    def close(self):
        self._driver.close()

    def quit(self):
        self._driver.quit()

















