import sys
import unittest
from config import readconfig
from engine.parsekeyword import ParseKeyword
from common.oracle import Oracle
from driver.driver import browser
from pages.base.basepage import BasePage
from pages.loginpage import LoginPage
import os
import time

class DemoTestCase(unittest.TestCase,BasePage):

    def setUp(self):
        self.driver = browser(readconfig.browser_name)
        LoginPage(self.driver).login(readconfig.login_user,readconfig.login_password)

    def tearDown(self):
        self.driver.quit()

    def _use_keyword(self,module_name,func_name,opvalues=None):
        func = ParseKeyword(self.driver).parse(module_name, func_name)
        if opvalues == "" or opvalues == None:
            func()
        else:
            opvalist = opvalues.split(',')
            func(*opvalist)

    @staticmethod
    def group(keyword_list):
        def func(self):
            try:
                for i in range(len(keyword_list)):
                    key_info = keyword_list[i]
                    self._use_keyword(key_info["PMODULE"], key_info["ACTION"], key_info["OPVALUES"])
            except Exception as e:
                raise e

        return func

def _generate_testcases(testcaseid_list):
    if testcaseid_list == []:
        return
    oracle = Oracle(readconfig.db_url)
    loop_kwlist = []

    for tl in testcaseid_list:
        tcid = tl['TCID']
        loop_kwlist = oracle.dict_fetchall("select * from xf_tcdata where tcid='%s'"%tcid)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + tcid, func)
        loop_kwlist = []

    oracle.close()

def _generate_mix_testcase(suite_list):
    if suite_list == []:
        return
    loop_kwlist = []
    oracle = Oracle(readconfig.db_url)

    for sl in suite_list:
        tmid = sl['TMID']
        tcid_list = sl['TCID'].split(',')
        tcids = str(tuple(tcid_list))
        loop_kwlist = oracle.dict_fetchall('select * from xf_tcdata where tcid in %s'%tcids)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + tmid, func)
        loop_kwlist = []
    oracle.close()

def _generate_testsuite(testcaseid_list,tmid_list):
    if testcaseid_list == [] and tmid_list == []:
        return
    caseid_list = []
    for tl in testcaseid_list:
        tcid = tl['TCID']
        tcid = 'test_' + tcid
        caseid_list.append(tcid)
    for tl in tmid_list:
        tmid = tl['TMID']
        tmid = 'test_' + tmid
        caseid_list.append(tmid)
    suite = unittest.TestSuite(map(DemoTestCase, caseid_list))
    return suite

oracle = Oracle(readconfig.db_url)

testcaseid_list = oracle.dict_fetchall("select distinct tcid from xf_tcdata order by tcid")
suite_list = oracle.dict_fetchall("select * from xf_tsuite order by tmid")
tmid_list = oracle.dict_fetchall('select tmid from xf_tsuite')

_generate_testcases(testcaseid_list)
# _generate_mix_testcase(suite_list)
group_testsuite = _generate_testsuite(testcaseid_list,tmid_list)
if type(group_testsuite) == str:
     print('please add data to xf_tcdata or xf_tsuite')

oracle.close()

if __name__ == "__main__":
    unittest.TextTestRunner().run(group_testsuite)
#     result = unittest.main(verbosity=2)




