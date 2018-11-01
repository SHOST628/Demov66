import os
import unittest
from random import choice
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import readconfig
from pages.base.keyword import Action


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # self.driver = webdriver.Chrome()
        cur_dir = os.path.dirname(os.getcwd())
        driver_path = cur_dir + "/driver"
        os.environ["PATH"] = os.environ["PATH"] + ';' + driver_path
        global driver
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        # option.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=option)
        sleep(1)
        driver.get(readconfig.url)
        # # print(driver.capabilities['version'])

        pass


    @classmethod
    def tearDownClass(cls):
        # try:
        #     driver.refresh()
        # except ConnectionRefusedError as e:
        #     print(e)
        driver.quit()
    def setUp(self):
        pass

    def tearDown(self):
        driver.refresh()
        # sleep(2)

    def test_login(self):
        """testcase login"""
        try:
            obj = Action(driver)
            print(driver.get_cookies())
            driver.find_element_by_xpath(".//*[@id='xf_staffcode']/input").clear()
            # driver.switch_to.active_element.send_keys("666")
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='xf_staffcode']/input"))).send_keys("666")

            # driver.find_element_by_xpath(".//*[@id='xf_staffcode']/input").send_keys("666")
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            # driver.find_element_by_xpath(".//*[@id='xf_password']").clear()
            # driver.switch_to.active_element.send_keys("666")
            obj.input_text(".//*[@id='xf_password']",'666')
            # driver.find_element_by_xpath(".//*[@id='xf_password']").send_keys("666")
            # driver.find_element_by_xpath("//div[@id='languagetype']/div").click()
            # driver.find_element_by_xpath("//span[contains(text(),'简体中文 ( zh_CN )')]").click()
            driver.find_element_by_xpath(".//*[@id='okbtn']/span/span").click()
            # obj.click("//span[contains(text(),'系统菜单')]")
            obj.click("//span[contains(text(),'系统设定')]")
            obj.click("//span[contains(text(),'后台系统设定')]")
            obj.click("//span[contains(text(),'区域维护')]")
        #     sleep(3)
        #     print(driver.get_cookies())
        #     sleep(2)
        #     # print("aftercookie: %s"%driver.get_cookies())
        # #     cookie = driver.get_cookies()
        #     driver.delete_all_cookies()
        #     sleep(2)
        #     print(driver.get_cookies())
        #     driver.add_cookie()
        #     sleep(1)
        #     # url = 'http://172.31.2.234:8186/stp65/'
        #     # driver.get(url)
        #     driver.add_cookie(cookie[0])
        #     print(driver.get_cookies())
        #     sleep(1)
        #     driver.refresh()
        #     sleep(3)
        #     driver.find_element_by_xpath(".//*[@id='xf_staffcode']/input").clear()
        #     # driver.switch_to.active_element.send_keys("666")
        #     WebDriverWait(driver, 5).until(
        #         EC.visibility_of_element_located((By.XPATH, ".//*[@id='xf_staffcode']/input"))).send_keys("666")
        #     # driver.find_element_by_xpath(".//*[@id='xf_staffcode']/input").send_keys("666")
        #     driver.switch_to.active_element.send_keys(Keys.ENTER)
        #     driver.find_element_by_xpath(".//*[@id='xf_password']").clear()
        #     driver.switch_to.active_element.send_keys("666")
        #     # driver.find_element_by_xpath(".//*[@id='xf_password']").send_keys("666")
        #     driver.find_element_by_xpath("//div[@id='languagetype']/div").click()
        #     driver.find_element_by_xpath("//span[contains(text(),'简体中文 ( zh_CN )')]").click()
        except Exception as e:
            raise e

    # def test_other(self):
    #     driver.find_element_by_xpath(".//span[contains(text(),'价格与促销')]").click()
    #     driver.find_element_by_xpath(".//span[contains(text(),'促销')]").click()
    #     driver.find_element_by_xpath(".//span[contains(text(),'贵宾管理')]").click()
    #     driver.find_element_by_xpath(".//span[contains(text(),'内容管理')]").click()


    # def test_region_maintenace(self):
    #     """new a region"""
    #
    #     try:
    #         sleep(1)
    #         # driver.find_element_by_xpath("//div[@class='v-slot']/div/div/div/div/div[contains(text(),'系统菜单')]").click()
    #         driver.find_element_by_xpath("//div[@class='v-slot']/div/div[1]/div[1]/div/div").click() #system menu
    #         driver.find_element_by_xpath("//div[@role='tree']/div[1]/div[1]/div/span").click() #System Configuration
    #         driver.find_element_by_xpath("//div[@role='tree']/div[1]/div[2]/div[2]/div[1]/div/span").click() #Backend System Configuraton
    #         driver.find_element_by_xpath("//div[@role='treeitem']/div[1]/div/span[contains(text(),'Region')]").click() #Region Mataintenace
    #         sleep(1)
    #         driver.find_element_by_xpath("//div[@class='v-slot']/div/div/div[4]/div/span[2]/span").click() #the button of New(common)
    #         # driver.find_element_by_xpath('//*[@id="XF_REGIONCODE"]').send_keys('CN')
    #         sleep(1)
    #         driver.find_element_by_css_selector('#XF_REGIONCODE').send_keys('CN')
    #         driver.find_element_by_css_selector('#XF_NAME').send_keys('China')
    #         driver.find_element_by_css_selector('#XF_COUNTRY').send_keys('China')
    #         driver.find_element_by_css_selector('#XF_DESCI').send_keys('RMB')
    #         # driver.find_element_by_xpath('//span[contains(text(),"Clear")]').click()  #the button of Clear (common)
    #
    #         basepage = BasePage(driver)
    #         driver.find_element_by_xpath('//*[@id="XF_BASECURRCODE"]/div').click()
    #
    #         #choose a random option of drop down list
    #         currency_list = basepage.find_elements((By.XPATH,"//div[@class='v-filterselect-suggestmenu']/table/tbody//span"))
    #         del currency_list[:2]
    #         choice(currency_list).click()
    #         # BasePage(driver).rselect('//*[@id="XF_BASECURRCODE"]/div','//div[@class="v-filterselect-suggestmenu"]/table/tbody//span')
    #
    #
    #
    #         # driver.find_element_by_xpath('//*[@id="XF_PRICEINCLUDETAX"]/div').click()
    #         # el = driver.find_element_by_xpath('//div[@class="v-filterselect-suggestmenu"]/table/tbody')
    #         # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[contains(text(),"Include Tax (2)")]'))).click()
    #         basepage.select((By.XPATH, "//*[@id='XF_PRICEINCLUDETAX']/div"), "Include Tax (2)")
    #
    #         driver.find_element_by_xpath('//span[contains(text(),"Exit")]').click()  #the button of Exit (common)
    #         # print(driver.switch_to.alert.text)
    #         # driver.switch_to.alert.accept()
    #         driver.find_element_by_xpath('//span[text()="Yes"]').click()  #clicked "yes"  after prompting and the prompt is unofficial  (common)
    #         sleep(1)
    #         # al = EC.alert_is_present()(driver)
    #         # if al:
    #         #     print(al.text)
    #         # else:
    #         #     print("no alert open")
    #         content = driver.find_element_by_xpath('//*[@id="stp65-109770030-overlays"]/div/div/div/p').text
    #         # self.assertTrue("success" in content, "can't not new a region")
    #         self.assertNotIn("Error", content, "can't not new a region")
    #
    #     except Exception as e:
    #         report_path = readconfig.report_path + '/new_rgeion_error.png'
    #         driver.save_screenshot(report_path)
    #         raise e
    #
    # def test_del_region(self):
    #     """choose a region to delete"""
    #     try:
    #         table = driver.find_element_by_xpath("//table[@class='v-table-table']/tbody")
    #         table.find_element_by_xpath("//div[contains(text(),'CN')]").click()
    #         driver.find_element_by_xpath("//span[contains(text(),'Modify')]").click()
    #         # driver.find_element_by_xpath("//span[contains(text(),'Delete')]").click()
    #         # driver.find_element_by_xpath("//span[contains(text(),'Confirm')]").click()
    #         # driver.find_element_by_css_selector("#XF_NAME").clear()
    #         # driver.find_element_by_css_selector("#XF_NAME").send_keys("CHINA")
    #         driver.find_element_by_xpath("//input[@id='XF_NAME']").clear()
    #         driver.find_element_by_xpath("//input[@id='XF_NAME']").send_keys("CHINA")
    #         driver.find_element_by_xpath("//span[contains(text(),'Exit')]").click()
    #         driver.find_element_by_xpath("//span[contains(text(),'Yes')]").click()
    #
    #     except Exception as e:
    #         report_path = readconfig.report_path + '/del_region_error.png'
    #         driver.save_screenshot(report_path)
    #
    #         raise e

def testsuite():
    suite1 = unittest.TestSuite()
    suite1.addTest(MyTestCase("test_login"))
    # suite1.addTest(MyTestCase("test_del_region"))
    # suite2 = unittest.TestSuite()
    # suite2.addTest(MyTestCase("test_region_maintenace"))
    suite = unittest.TestSuite([suite1])
    # suite.addTest(MyTestCase("test_login"))
    # suite.addTest(MyTestCase("test_region_maintenace"))
    # suite.addTest(MyTestCase("test_del_region"))
    return suite

def testsuite1():
    suite = unittest.TestLoader().loadTestFromTestCase(MyTestCase)
    return suite

def testsuite2():
    tests = ["test_login","test_region_maintenace","test_del_region"]
    suite = unittest.TestSuite(map(MyTestCase,tests))
    return suite

if __name__ == "__main__":
    # unittest.TextTestRunner().run(testsuite())
    unittest.TextTestRunner().run(testsuite())
    # unittest.TextTestRunner().run(testsuite2())
    # unittest.main()




