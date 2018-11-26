from common.HTMLTestRunner import HTMLTestRunner
from engine.executionengine import testsuite
import time
from common.file import mkdir
from common.logger import logger
# from tomorrow import threads
# import threading
# _lock = threading.RLock()
# _cond = threading.Condition(lock=_lock)

# @threads(2)
def run(testsuite):
    report_title = "测试报告"
    curtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    report_folder = '../report/htmlreport'
    mkdir(report_folder)
    report_path = '../report/htmlreport/%s_Report.html' % (curtime)
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description="")
        runner.run(testsuite)

if __name__ == "__main__":
    if testsuite:
        logger.info("【开始执行用例】")
        # report_title = "测试报告"
        # curtime = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        # report_folder = '../report/htmlreport'
        # mkdir(report_folder)
        # report_path = '../report/htmlreport/%s_Report.html'%(curtime)
        # with open(report_path,'wb') as report:
        #     runner = HTMLTestRunner(stream=report,title=report_title,description="")
        #     runner.run(testsuite)
        # for case in testsuite:
        #     _cond.acquire()
        #     run(case)
        #     _cond.release()
        try:
            run(testsuite)
        except Exception as e:
            logger.exception(e)
        logger.info("【结束执行用例】")
        logger.info("")




