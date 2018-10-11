from test.testc import testsuite
from test.HTMLTestRunner_ import HTMLTestRunner
import time

if __name__ == "__main__":
    report_title = "测试报告"
    curtime = time.strftime("%Y%m%d_%H%M%S",time.localtime())
    report_path = '../report/'+ curtime +'_Report.html'
    with open(report_path,'wb') as report:
        runner = HTMLTestRunner(stream=report,title=report_title,description="")
        runner.run(testsuite())






