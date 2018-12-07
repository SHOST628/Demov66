import os
from selenium import webdriver
from common.logger import logger


def browser(browser_type):
    try:
        cur_dir = os.path.dirname(os.getcwd())
        driver_path = os.path.join(cur_dir,'driver')
        os.environ["PATH"] = os.environ["PATH"] + ';' + driver_path
        browser_type = browser_type.lower()
        if browser_type == "chrome": # chrome version:70.0.3.3538.77 (64bit)
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Chrome(chrome_options=option)
            # version = driver.capabilities['version']
            return driver

        elif (browser_type == "firefox"):
            pass

        else:
            pass

        # return driver
    except Exception as e:
        logger.exception(e)