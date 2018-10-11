import sys
import unittest
from config import readconfig
from engine.parsekeyword import ParseKeyword
from common.oracle import Oracle
from driver.driver import browser
from pages.base.basepage import BasePage
import os
import time

class DemoTestCase(unittest.TestCase,BasePage):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser(readconfig.browser_name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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

def _generate_testcases(keyword_list):
    testcaseid_list = []
    loop_kwlist = []

    # get all testcaseid from testcase table
    for d in keyword_list:
        tcid = d['TCID']
        if tcid not in testcaseid_list:
            testcaseid_list.append(tcid)

    # need to be fixed?how
    for l in testcaseid_list:
        for d in keyword_list:
            values = list(d.values())
            if l in values:
                loop_kwlist.append(d)
        func = DemoTestCase.group(loop_kwlist)
        setattr(DemoTestCase, 'test_' + l, func)
        loop_kwlist = []

def _generate_testsuite(tcid):
    """new a testsuite"""
    tcid_list = tcid.split(',')
    tests = []
    for tl in tcid_list:
        tl = "test_" + tl
        tests.append(tl)
    suite = unittest.TestSuite(map(DemoTestCase,tests))
    return suite

def _group_testsuite(tsuite_list):
    """group all testsuite"""
    create_suite = None
    suite_list = []
    for tl in tsuite_list:
        tcid = tl['TCID']
        create_suite = _generate_testsuite(tcid)
        suite_list.append(create_suite)
    suite = unittest.TestSuite(suite_list)
    return suite


oracle = Oracle(readconfig.db_url)
keyword_list = oracle.dict_fetchall("select * from xf_tcdata order by tcid,tsid")
_generate_testcases(keyword_list)

suite_list = oracle.dict_fetchall("select * from xf_tsuite order by tmid")
group_testsuite = _group_testsuite(suite_list)

oracle.close()

if __name__ == "__main__":
    unittest.TextTestRunner().run(group_testsuite)
#     result = unittest.main(verbosity=2)




