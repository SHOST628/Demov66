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
        logger.info("找不到基础用例信息")
        return None
    oracle = Oracle(readconfig.db_url)
    # loop_kwlist = []
    global exclude_caseid_list
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
                exclude_caseid_list.append(caseid)
            else:
                func = DemoTestCase.group(loop_kwlist)
                setattr(DemoTestCase, 'test_' + caseid, func)
                logger.info("已生成用例 test_%s" % caseid)
        else:
            logger.info("找不到该用例id %s，无法生成用例 test_%s" % (caseid,caseid))
            exclude_caseid_list.append(caseid)
    logger.info("<基础测试用例生成结束>")
        # loop_kwlist = []

    oracle.close()

#TODO need to fix
def _generate_mix_testcase(mixcase_list):
    if mixcase_list == []:
        logger.info("没有需要组合的用例")
        return None
    # loop_kwlist = []
    oracle = Oracle(readconfig.db_url)
    global exclude_mixid_list
    #  notice the order of testcase execution
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
            setattr(DemoTestCase, 'test_' + mixid, func)
            logger.info("已生成组合用例 test_%s" % mixid)
        else:
            exclude_mixid_list.append(mixid)
            logger.info("无法查询到基础用例id %s , 组合用例id %s 无法生成组合用例" % (caseid_list,mixid))
        # loop_kwlist = []
    logger.info("<组合测试用例生成结束>")
    oracle.close()

def _generate_testsuite(testcaseid_list,mixid_list):
    if testcaseid_list == [] and mixid_list == []:
        logger.info("缺少用例数据，请指定或者添加相应的用例数据")
        return None
    caseid_list = []
    global exclude_caseid_list
    logger.info("<开始加载测试用例>")
    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        if caseid not in exclude_caseid_list:
            caseid = 'test_' + caseid
            caseid_list.append(caseid)
    logger.info("已加载基础测试用例 %s" % caseid_list)
    for tl in mixid_list:
        mixid = tl['XF_MIXID']
        if mixid == None or mixid == '':
            pass
        elif mixid in exclude_mixid_list:
            logger.info("组合用例id %s 没有基础用例信息，无法加载" % mixid)
        else:
            mixid = 'test_' + mixid
            caseid_list.append(mixid)
    logger.info("已加载全部测试用例 %s" % caseid_list)
    logger.info("<测试用例加载结束>")
    logger.debug("<开始组合测试套件>")
    suite = unittest.TestSuite(map(DemoTestCase, caseid_list))
    logger.debug("已组合全部测试套件 %s" % suite)
    logger.debug("<测试套件组合结束>")
    return suite

oracle = Oracle(readconfig.db_url)
Flag = readconfig.debug_mode

exclude_caseid_list = [] # exclude base testcases that can't run alone
exclude_mixid_list = [] # exclude mix testcase that can not run alone

# deciding execute all testcases or debug some testcases controling by the config mode in ini,if mode == 1, debug case,else execute all testcases
# the config executeuser deciding whose testcase to execute
if Flag:
    logger.info("***调试模式***")
    execute_user = readconfig.execute_user
    if execute_user == '':
        sql = "select xf_caseid from xf_casedebug where xf_executeuser is null order by xf_caseid"
        testcaseid_list = oracle.dict_fetchall(sql)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser is null order by xf_mixid"
        mixid_list = oracle.dict_fetchall(sql)
    else:
        sql = "select xf_caseid from xf_casedebug where xf_executeuser = '%s' order by xf_caseid" % execute_user
        testcaseid_list = oracle.dict_fetchall(sql)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser = '%s' order by xf_mixid" % execute_user
        mixid_list = oracle.dict_fetchall(sql)
    mixcase_list = []
    for i in mixid_list:
        mixid = i["XF_MIXID"]
        if mixid:
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




