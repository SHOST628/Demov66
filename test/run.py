# from common.HTMLTestRunner import HTMLTestRunner
from HtmlTestRunner import HTMLTestRunner
from engine.executionengine import testsuite
import time

if __name__ == "__main__":
    report_title = "测试报告"
    curtime = time.strftime("%Y%m%d_%H%M%S",time.localtime())
    report_path = '../report/htmlreport/%s_Report.html'%(curtime)
    # with open(report_path,'wb') as report:
    #     # runner = HTMLTestRunner(stream=report,title=report_title,description="")
    #     runner = HTMLTestRunner(output=report, report_title=report_title, descriptions="")
    #     runner.run(testsuite)


    runner = HTMLTestRunner(output=report_path, report_title=report_title, descriptions="")
    runner.run(testsuite)