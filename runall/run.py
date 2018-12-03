from common.HTMLTestRunner import HTMLTestRunner
from engine.executionengine import testsuite
import time
from common.file import mkdir
from common.logger import logger
from config import readconfig
from common.mail import Mail
import os
# from tomorrow import threads
# import threading
# _lock = threading.RLock()
# _cond = threading.Condition(lock=_lock)

report_path = ''
# @threads(2)
def run(testsuite):
    report_title = "测试报告"
    curtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    if readconfig.report_path == '':
        report_folder = os.path.dirname(os.getcwd()) + '\\report\\htmlreport'
        mkdir(report_folder)
    else:
        report_folder = readconfig.report_path
        mkdir(report_folder)
    global report_path
    report_name = '%s_Report.html' % curtime
    report_path = os.path.join(report_folder,report_name)
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
        #     run(case)
        try:
            run(testsuite)
        except Exception as e:
            logger.exception(e)
        logger.info("【结束执行用例】")
        logger.info("")
        flag = int(readconfig.if_send)
        if flag:
            logger.info("【正在发送邮件报告】")
            mail = Mail(readconfig.email_host,readconfig.email_user,readconfig.email_psw)
            content = "自动化测试已结束，请查收测试报告"
            mail.send_mail(readconfig.Receivers, '自动化测试报告', content, report_path)
            logger.info("【邮件报告发送结束】")
            logger.info("")
    else:
        logger.info("缺少用例数据，请指定或者添加相应的用例数据")
        logger.info("")



