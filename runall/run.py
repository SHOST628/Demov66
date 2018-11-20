from common.HTMLTestRunner import HTMLTestRunner
from engine.executionengine import testsuite
import time
from common.file import mkdir
from common.logger import logger

if __name__ == "__main__":
    if testsuite:
        logger.info("【开始执行用例】")
        report_title = "测试报告"
        curtime = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        report_folder = '../report/htmlreport'
        mkdir(report_folder)
        report_path = '../report/htmlreport/%s_Report.html'%(curtime)
        with open(report_path,'wb') as report:
            runner = HTMLTestRunner(stream=report,title=report_title,description="")
            runner.run(testsuite)
        logger.info("【结束执行用例】")
        logger.info("")
    else:
        logger.info('缺少用例数据，请指定或者添加相应的用例数据')






