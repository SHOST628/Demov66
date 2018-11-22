import sys
import unittest
from config import readconfig
from engine.parsekeyword import ParseKeyword
from common.oracle import Oracle
from driver.driver import browser
from pages.base.keyword import Action
from pages.loginpage import LoginPage
from common.storage import Storage
import re
import os
import time
from common.logger import logger
from common.logger import sql_log

class DemoTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = browser(readconfig.browser_name)
        self.driver.maximize_window()
        LoginPage(self.driver).login(readconfig.login_user,readconfig.login_password)

    def tearDown(self):
        logger.info('***************************************************END***************************************************')
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
                    if hasattr(Storage,var):
                        var_value = getattr(Storage,var)
                        opvalues = re.sub("\$(.+?)\$",var_value,opvalues,count=1)
                        logger.info("变量 %s 的值为 %s"%(var,var_value))
                except AttributeError as e:
                    logger.error("找不到变量 %s" % var)
                    raise e
            opvalist = opvalues.split('##')
            func(*opvalist)

    @staticmethod
    def group(keyword_list):
        def func(self):
            logger.info('**************************************************START**************************************************')
            if keyword_list != []:
                for key_dict in keyword_list:
                    try:
                        logger.info('正在执行用例 %s 的 %s %s %s %s' % (
                            key_dict["XF_CASEID"], key_dict["XF_TSID"], key_dict["XF_TSDESC"], key_dict["XF_ACTION"],
                            key_dict["XF_OPVALUES"]))
                        self._use_keyword(key_dict["XF_ACTION"], key_dict["XF_OPVALUES"])
                    except Exception as e:
                        logger.error('执行用例 %s 的 %s %s %s %s 出错' % (
                            key_dict["XF_CASEID"], key_dict["XF_TSID"], key_dict["XF_TSDESC"], key_dict["XF_ACTION"],
                            key_dict["XF_OPVALUES"]))
                        logger.exception(e)
                        raise e
            else:
                logger.info("没有查询到该用例，无法执行")
                self.assertFalse(True)
        return func

def _generate_testcases(testcaseid_list):
    if testcaseid_list == []:
        return None
    oracle = Oracle(readconfig.db_url)
    # loop_kwlist = []

    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        #  notice  the order of step execution
        sql = "select * from xf_testcase where xf_caseid='%s' order by xf_tsid"%caseid
        loop_kwlist = oracle.dict_fetchall(sql)
        sql_log(logger,sql,loop_kwlist)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + caseid, func)
        # loop_kwlist = []

    oracle.close()

#TODO need to fix
def _generate_mix_testcase(mixcase_list):
    if mixcase_list == []:
        return None
    # loop_kwlist = []
    oracle = Oracle(readconfig.db_url)
    #  notice the order of testcase execution
    for sl in mixcase_list:
        mixid = sl['XF_MIXID']
        caseid_list = sl['XF_CASEID'].split(',')
        caseid_str = ','.join(caseid_list)
        caseids = str(tuple(caseid_list))
        #order by caseid,tsid
        sql = "select * from xf_testcase where xf_caseid in %s \
        order by instr('%s',rtrim(cast(xf_caseid as nchar))),xf_tsid"%(caseids,caseid_str)
        loop_kwlist = oracle.dict_fetchall(sql)
        sql_log(logger,sql,loop_kwlist)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + mixid, func)
        # loop_kwlist = []
    oracle.close()

def _generate_testsuite(testcaseid_list,mixid_list):
    if testcaseid_list == [] and mixid_list == []:
        return None
    caseid_list = []
    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        caseid = 'test_' + caseid
        caseid_list.append(caseid)
    for tl in mixid_list:
        mixid = tl['XF_MIXID']
        if mixid == None or mixid == '':
            pass
        else:
            mixid = 'test_' + mixid
            caseid_list.append(mixid)
    suite = unittest.TestSuite(map(DemoTestCase, caseid_list))
    return suite

oracle = Oracle(readconfig.db_url)
Flag = readconfig.debug_mode

# deciding execute all testcases or debug some testcases control by the config mode in ini,if mode == 1, debug case,else execute all testcases
# the config executeuser deciding whose testcase to execute
if not Flag:
    sql = "select distinct xf_caseid from xf_testcase"
    testcaseid_list = oracle.dict_fetchall(sql)
    sql_log(logger,sql,testcaseid_list)
    sql = "select * from xf_mixcase"
    mixcase_list = oracle.dict_fetchall(sql)
    sql_log(logger,sql,mixcase_list)
    sql = "select xf_mixid from xf_mixcase"
    mixid_list = oracle.dict_fetchall(sql)
    sql_log(logger,sql,mixid_list)
else:
    execute_user = readconfig.execute_user
    if execute_user == '':
        sql = "select xf_caseid from xf_casedebug where xf_executeuser is null order by xf_caseid"
        testcaseid_list = oracle.dict_fetchall(sql)
        sql_log(logger,sql,testcaseid_list)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser is null order by xf_mixid"
        mixid_list = oracle.dict_fetchall(sql)
        sql_log(logger,sql,mixid_list)
    else:
        sql = "select xf_caseid from xf_casedebug where xf_executeuser = '%s' order by xf_caseid" % execute_user
        testcaseid_list = oracle.dict_fetchall(sql)
        sql_log(logger,sql,testcaseid_list)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser = '%s' order by xf_mixid" % execute_user
        mixid_list = oracle.dict_fetchall(sql)
        sql_log(logger,sql,mixid_list)
    mixcase_list = []
    for i in mixid_list:
        mixid = i.values()
        sql = "select * from xf_mixcase where xf_mixid = '%s'" % mixid
        mixcase_list = mixcase_list + oracle.dict_fetchall(sql)
    sql_log(logger,sql,mixcase_list)

_generate_testcases(testcaseid_list)
_generate_mix_testcase(mixcase_list)
testsuite = _generate_testsuite(testcaseid_list, mixid_list = [])

oracle.close()

if __name__ == "__main__":
    unittest.TextTestRunner().run(testsuite)
    result = unittest.main(verbosity=2)




