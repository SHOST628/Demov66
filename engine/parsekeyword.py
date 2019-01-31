from pages.keywords.actionkeyword import Action
from common.logger import logger

class ParseKeyword(object):
    def __init__(self,driver):
        self.driver = driver

    def parse(self,func_name):
        try:
                obj = Action(self.driver)
                if hasattr(obj,func_name):
                    func = getattr(obj,func_name)
                    return func
                else:
                    logger.info("找不到该关键字:%s"%func_name)

        except Exception as e:
            raise e



