from pages.base.keyword import Action

def add(func):  # 增加打印日志的方法
    def wrapper(self, first, second, msg=None):
        try:
            func(self, first, second, msg=None)

        except AssertionError:
            Action().save_screenshot()
            raise AssertionError(msg)  # 抛出AssertionError

    return wrapper