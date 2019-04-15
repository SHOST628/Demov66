import sys
import unittest
from config import readconfig
from engine.parsekeyword import ParseKeyword
from common.oracle import Oracle
from driver.driver import browser
from pages.keywords.keyword import BaseKeyword
from pages.loginpage import LoginPage
from common.storage import Storage
import re
import os
from datetime import datetime
from common.logger import logger
from selenium.common.exceptions import TimeoutException


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
                    if location_id == None:
                        opvalues = key_dict['XF_OPVALUES']
                        if opvalues == None:
                            self._use_keyword(key_dict["XF_ACTION"])
                        else:
                            self._use_keyword(key_dict["XF_ACTION"], opvalues)
                    else:
                        opvalues = key_dict['XF_OPVALUES']
                        location = self.get_location(location_id)  # get loaction value
                        if opvalues == None:
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


def _set_method_info(method_name, desc, cls):
    """
    set description for testcase
    :param method_name:
    :param desc: testcase description
    :param cls: class name
    :return:
    """
    func = getattr(cls,method_name)
    func.__doc__ = desc


def _generate_testcases(testcaseid_list):
    if testcaseid_list == []:
        logger.info("找不到基础用例信息")
        return None
    oracle = Oracle(readconfig.db_url)
    logger.info("<开始生成基础测试用例>")
    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        #  notice  the order of step execution
        sql = "select * from xf_testcase where xf_caseid='%s' order by xf_tsid"%caseid
        loop_kwlist = oracle.dict_fetchall(sql)
        if loop_kwlist:
            ifmix = loop_kwlist[0]['XF_IFMIX']  # it will not execute the case if ifmix larger than 0
            if ifmix:
                logger.info("测试用例 %s 不能单独执行" % caseid)
            else:
                func = DemoTestCase.group(loop_kwlist)
                method_name = "test_" + caseid
                setattr(DemoTestCase, method_name, func)
                logger.info("已生成用例 %s" % method_name)
                _set_method_info(method_name,loop_kwlist[0]["XF_CASEDESC"],DemoTestCase)
        else:
            logger.info("找不到该用例id %s，无法生成用例 test_%s" % (caseid,caseid))
    logger.info("<基础测试用例生成结束>")

    oracle.close()


# bug: it can  still generate mix testcase if has a true caseid although contains false caseid
def _generate_mix_testcase(mixcase_list):
    if mixcase_list == []:
        logger.info("没有需要组合的用例")
        return None
    oracle = Oracle(readconfig.db_url)
    logger.info("<开始生成组合测试用例>")
    for sl in mixcase_list:
        mixid = sl['XF_MIXID']
        caseid_list = sl['XF_CASEID'].split(',')
        caseid_str = ','.join(caseid_list)
        caseids = str(tuple(caseid_list))
        if len(caseid_list) == 1:
            caseids = caseids.replace(',','')
        #order by caseid,tsid
        sql = "select * from xf_testcase where xf_caseid in %s " \
              "order by instr('%s',rtrim(cast(xf_caseid as nchar))),xf_tsid"%(caseids,caseid_str)
        loop_kwlist = oracle.dict_fetchall(sql)
        if loop_kwlist:
            func = DemoTestCase.group(loop_kwlist)
            method_name = "test_" + mixid
            setattr(DemoTestCase, method_name, func)
            logger.info("已生成组合用例 %s ,包含基础用例id %s" % (method_name,caseid_list))
            _set_method_info(method_name,sl["XF_MIXCASEDESC"],DemoTestCase)
        else:
            logger.info("基础用例id %s 错误,无法生成组合用例 test_%s " % (caseid_list,mixid))

    logger.info("<组合测试用例生成结束>")
    oracle.close()

# todo notice
# another method to generate testsuite is that finds test method name containing character test
# by dir method,but order by method name
def _generate_testsuite(testcaseid_list,mixid_list):
    if testcaseid_list == [] and mixid_list == []:
        return None
    caseid_list = []
    logger.info("<开始加载测试用例>")
    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        test_method_id = 'test_' + caseid
        if hasattr(DemoTestCase,test_method_id):
            caseid_list.append(test_method_id)
        else:
            logger.info("无法加载基础测试用例id %s " % caseid)
    logger.info("已加载基础测试用例 %s" % caseid_list)
    for tl in mixid_list:
        mixid = tl['XF_MIXID']
        test_method_id = 'test_' + mixid
        if hasattr(DemoTestCase,test_method_id):
            caseid_list.append(test_method_id)
        else:
            logger.info("组合用例id %s 没有基础用例信息，无法加载" % mixid)
    logger.info("已加载全部测试用例 %s" % caseid_list)
    logger.info("<测试用例加载结束>")
    logger.debug("<开始组合测试套件>")
    suite = unittest.TestSuite(map(DemoTestCase, caseid_list))
    logger.debug("已组合全部测试套件 %s" % suite)
    logger.debug("<测试套件组合结束>")
    return suite


oracle = Oracle(readconfig.db_url)
Flag = readconfig.debug_mode


# deciding execute all testcases or debug some testcases controling by the config mode in ini,if mode == 1,
# debug case,else execute all testcases
# the config executeuser deciding whose testcase to execute
if Flag:
    logger.info("***调试模式***")
    execute_user = readconfig.execute_user
    if execute_user == '':
        sql = "select xf_caseid from xf_casedebug where xf_executeuser is null " \
              "and xf_caseid is not null order by xf_caseid"
        testcaseid_list = oracle.dict_fetchall(sql)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser is null " \
              "and xf_mixid is not null order by xf_mixid"
        mixid_list = oracle.dict_fetchall(sql)
    else:
        sql = "select xf_caseid from xf_casedebug where xf_executeuser = '%s' " \
              "and xf_caseid is not null order by xf_caseid" % execute_user
        testcaseid_list = oracle.dict_fetchall(sql)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser = '%s' " \
              "and xf_mixid is not null order by xf_mixid" % execute_user
        mixid_list = oracle.dict_fetchall(sql)
    mixcase_list = []
    for i in mixid_list:
        mixid = i["XF_MIXID"]
        sql = "select * from xf_mixcase where xf_mixid = '%s'" % mixid
        mixcase_list = mixcase_list + oracle.dict_fetchall(sql)
else:
    logger.info("***普通模式***")
    sql = "select distinct xf_caseid from xf_testcase"
    testcaseid_list = oracle.dict_fetchall(sql)
    sql = "select * from xf_mixcase"
    mixcase_list = oracle.dict_fetchall(sql)
    sql = "select xf_mixid from xf_mixcase"
    mixid_list = oracle.dict_fetchall(sql)


_generate_testcases(testcaseid_list)
_generate_mix_testcase(mixcase_list)
testsuite = _generate_testsuite(testcaseid_list, mixid_list)

oracle.close()

if __name__ == "__main__":
    unittest.TextTestRunner().run(testsuite)
    result = unittest.main(verbosity=2)




