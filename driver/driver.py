import os
from selenium import webdriver


def browser(browser_type):
    try:
        cur_dir = os.path.dirname(os.getcwd())
        driver_path = cur_dir + "/driver"
        os.environ["PATH"] = os.environ["PATH"] + ';' + driver_path
        browser_type = browser_type.lower()
        if browser_type == "chrome":
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Chrome(chrome_options=option)
            return driver

        elif (browser_type == "firefox"):
            pass

        else:
            pass

        # return driver
    except Exception as e:
        print(e)