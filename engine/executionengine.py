import sys
import unittest
from config import readconfig
from engine.parsekeyword import ParseKeyword
from common.oracle import Oracle
from driver.driver import browser
from pages.base.keyword import Action
from pages.loginpage import LoginPage
from common.storage import Storage
import os
import time

class DemoTestCase(unittest.TestCase, Action):

    def setUp(self):
        self.driver = browser(readconfig.browser_name)
        LoginPage(self.driver).login(readconfig.login_user,readconfig.login_password)

    def tearDown(self):
        self.driver.quit()

    def _use_keyword(self,func_name,opvalues=None):
        func = ParseKeyword(self.driver).parse(func_name)
        if opvalues == "" or opvalues == None:
            func()
        else:
            opvalist = opvalues.split('##')
            for i in range(len(opvalist)):
                # transfer a variate marked $$ to method
                if '$$' in opvalist[i]:
                    var_name = opvalist[i]
                    var_name = var_name[2:]
                    try:
                        if hasattr(Storage,var_name):
                            var_value = getattr(Storage,var_name,"找不到此变量%s"%var_name)
                            opvalist[i] = var_value
                    except Exception as e:
                        raise e
            func(*opvalist)

    @staticmethod
    def group(keyword_list):
        def func(self):
            try:
                for key_dict in keyword_list:
                    self._use_keyword(key_dict["XF_ACTION"], key_dict["XF_OPVALUES"])
            except Exception as e:
                raise e

        return func

def _generate_testcases(testcaseid_list):
    if testcaseid_list == []:
        return
    oracle = Oracle(readconfig.db_url)
    loop_kwlist = []

    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        #TODO notice  the order of step execution
        loop_kwlist = oracle.dict_fetchall("select * from xf_testcase where xf_caseid='%s' order by xf_tsid"%caseid)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + caseid, func)
        loop_kwlist = []

    oracle.close()

#TODO need to fix
def _generate_mix_testcase(suite_list):
    if suite_list == []:
        return
    loop_kwlist = []
    oracle = Oracle(readconfig.db_url)
    #TODO notice the order of testcase execution
    for sl in suite_list:
        mixid = sl['XF_MIXID']
        caseid_list = sl['XF_CASEID'].split(',')
        caseids = str(tuple(caseid_list))
        loop_kwlist = oracle.dict_fetchall('select * from xf_testcase where xf_caseid in %s'%caseids)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + mixid, func)
        loop_kwlist = []
    oracle.close()

def _generate_testsuite(testcaseid_list,mixid_list):
    if testcaseid_list == [] and mixid_list == []:
        return
    caseid_list = []
    for tl in testcaseid_list:
        caseid = tl['XF_CASEID']
        caseid = 'test_' + caseid
        caseid_list.append(caseid)
    for tl in mixid_list:
        mixid = tl['XF_MIXID']
        mixid = 'test_' + mixid
        caseid_list.append(mixid)
    suite = unittest.TestSuite(map(DemoTestCase, caseid_list))
    return suite

oracle = Oracle(readconfig.db_url)

testcaseid_list = oracle.dict_fetchall("select distinct xf_caseid from xf_testcase")
mixcase_list = oracle.dict_fetchall("select * from xf_mixcase")
mixid_list = oracle.dict_fetchall('select xf_mixid from xf_mixcase')

_generate_testcases(testcaseid_list)
# _generate_mix_testcase(mixcase_list)
testsuite = _generate_testsuite(testcaseid_list, mixid_list)
if type(testsuite) == str:
     print('please add data to xf_testcase or xf_mixcase')

oracle.close()

if __name__ == "__main__":
    unittest.TextTestRunner().run(testsuite)
    result = unittest.main(verbosity=2)




