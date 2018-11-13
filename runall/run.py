from common.HTMLTestRunner import HTMLTestRunner
from engine.executionengine import testsuite
import time
from common.file import mkdir

if __name__ == "__main__":
    report_title = "测试报告"
    curtime = time.strftime("%Y%m%d_%H%M%S",time.localtime())
    report_folder = '../report/htmlreport'
    mkdir(report_folder)
    report_path = '../report/htmlreport/%s_Report.html'%(curtime)
    with open(report_path,'wb') as report:
        runner = HTMLTestRunner(stream=report,title=report_title,description="")
        runner.run(testsuite)






