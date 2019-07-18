import sys
import unittest
from config import readconfig
from engine.parsekeyword import ParseKeyword
from common.oracle import Oracle
from driver.driver import browser
from pages.loginpage import LoginPage
from common.storage import Storage
import re
from datetime import datetime
from common.logger import logger


class DemoTestCase(unittest.TestCase):

    def setUp(self):
        self.start_time = datetime.now()
        self.driver = browser(readconfig.browser_name)
        self.driver.maximize_window()
        LoginPage(self.driver).login(readconfig.login_user,readconfig.login_password)

    def tearDown(self):
        logger.info('***************************************************END***************************************************')
        duration = datetime.now() - self.start_time
        logger.info("执行用例时间: %s " % duration)
        # self.driver.quit()

    def _use_keyword(self,func_name,opvalues=None):
        func = ParseKeyword(self.driver).parse(func_name)
        if opvalues == "" or opvalues == None:
            func()
        else:
            #  parse a variate from user defining
            var_list = re.findall("\$(.+?)\$",opvalues)
            for var in var_list:
                try:
                    var_value = getattr(Storage,var)
                    opvalues = re.sub("\$(.+?)\$",var_value,opvalues,count=1)
                    logger.info("变量 %s 的值为 %s"%(var,var_value))
                except AttributeError as e:
                    logger.error("找不到变量 %s" % var)
                    raise e
            opvalist = opvalues.split('##')
            func(*opvalist)

    def get_location(self,location_id):
        oracle = Oracle(readconfig.db_url)
        sql = "select xf_location from xf_pagelocation where xf_locationid = '%s'" % location_id
        location_list = oracle.dict_fetchall(sql)
        if not location_list:
            raise Exception("错误location_id ：%s，无法找到对应的location" % location_id)
        location = location_list[0]['XF_LOCATION']
        # clear string blank
        location = location.strip()
        # complement the location
        # solve problem: prevent location id from maintain many time
        # for example: add row case: location id change by rule
        if "%s" in location:
            location_ = location
            location_ = location.replace("%s", "")
            match_value = (re.findall("\[(.+?)\]",location_))[0]    # match a value in []
            match_value = match_value.replace("=",",")
            # change location format to "[contains(@id,XXX)]"  from [@id="XXX"]
            rep_value = "[contains(" + match_value + ")]"
            location_ = re.sub("\[(.+?)\]",rep_value,location_,count=1)
            count = len(self.driver.find_elements_by_xpath(location_)) - 1
            # count = self._use_keyword("count_elements", location_) - 1
            location = location.replace("%s", str(count))
        return location

    @staticmethod
    def group(keyword_list):
        def func(self):
            logger.info('**************************************************START**************************************************')
            location_id = ''
            opvalues = ''
            for key_dict in keyword_list:
                try:
                    logger.info('正在执行用例 %s 的 %s %s %s %s %s' % (
                        key_dict["XF_CASEID"], key_dict["XF_TSID"], key_dict["XF_TSDESC"], key_dict["XF_ACTION"],
                        key_dict["XF_LOCATIONID"],key_dict["XF_OPVALUES"]))
                    location_id = key_dict["XF_LOCATIONID"]
                    if location_id is None:
                        opvalues = key_dict['XF_OPVALUES']
                        if opvalues is None:
                            self._use_keyword(key_dict["XF_ACTION"])
                        else:
                            self._use_keyword(key_dict["XF_ACTION"], opvalues)
                    else:
                        opvalues = key_dict['XF_OPVALUES']
                        location = self.get_location(location_id)  # get loaction value
                        if opvalues is None:
                            self._use_keyword(key_dict["XF_ACTION"], location)
                        else:
                            if '##' in location:
                                location_element = location.split('##')
                                opvalues = location_element[0] + '##' + opvalues + location_element[1]
                            else:
                                opvalues = location + '##' + opvalues
                            self._use_keyword(key_dict["XF_ACTION"], opvalues)

                except Exception as e:
                    logger.info('执行用例 %s 的 %s %s %s %s %s 出错' % (
                        key_dict["XF_CASEID"], key_dict["XF_TSID"], key_dict["XF_TSDESC"], key_dict["XF_ACTION"],
                        key_dict["XF_LOCATIONID"], key_dict["XF_OPVALUES"]))
                    logger.exception(e)
                    raise e
        return func




