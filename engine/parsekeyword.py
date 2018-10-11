class ParseKeyword:
    def __init__(self,driver):
        self.driver = driver

    def parse(self,module_name,func_name):
        try:
            if '.' in module_name:
                index = module_name.rindex('.')
                class_name = module_name[index+1:]
                module_name = module_name[:index]
                obj = __import__("pages."+module_name,fromlist=True)
                if hasattr(obj,class_name):
                    obj = getattr(obj,class_name)
                    if hasattr(obj(self.driver),func_name):
                        func = getattr(obj(self.driver),func_name)
                        return func
                    else:
                        print("在该类:%s找不到方法:%s"%(class_name,func_name))
                else:
                    print("在模块:%s找不到该类:%s"%(module_name,class_name))
            else:
                obj = module_name
                if hasattr(obj(self.driver), func_name):
                    func = getattr(obj(self.driver), func_name)
                    return func
                else:
                    print("在该类:%s找不到方法:%s" % (module_name, func_name))

        except Exception as e:
            print(e)


