from pages.base.keyword import Action

class ParseKeyword:
    def __init__(self,driver):
        self.driver = driver

    def parse(self,func_name):
        try:
                obj = Action(self.driver)
                if hasattr(obj,func_name):
                    func = getattr(obj,func_name)
                    return func
                else:
                    print("找不到该关键字:%s"%func_name)

        except Exception as e:
            raise e



