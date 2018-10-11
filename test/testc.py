import unittest
# from engine.executionengine import group_testsuite

a=[False]

class Mydemo(unittest.TestCase):
    value = "This is a test \n testing"
    __doc__ = value
    def test1(self):
        try:
            print("i am test1")
            __doc__ = "this is a testMethod"
            print(__doc__)
        except Exception as e:
            a[0] = True
            raise e
    @unittest.skipIf(a[0],"test1 fail skip test2")
    def test2(self):
        try:
            print("i am test2")
            raise  AssertionError("error")
        except Exception as e:
            a[0] = True
            raise e
    @unittest.skipIf(a[0], "test1 fail skip test2")
    def test3(self):
        try:
            print(a[0])
            print("i am test3")
        except Exception as e:
            a[0] =True
            raise e

    @unittest.skipIf(True, "test skipping")
    def test4(self):
        try:
            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test5(self):
        try:
            print("i am test3")
            # print(3/0)
        except Exception as e:
            raise e

    def test6(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test7(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test8(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test9(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test10(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test11(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e



class MyDemo1(unittest.TestCase):

    def test12(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test13(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test14(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test15(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test16(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test17(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test18(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

    def test19(self):
        try:

            print("i am test3")
        except Exception as e:
            a[0] = True
            raise e

def testsuite():
    testsuite = unittest.TestLoader().loadTestsFromTestCase(Mydemo)
    testsuite1 = unittest.TestLoader().loadTestsFromTestCase(MyDemo1)
    suite = unittest.TestSuite([testsuite,testsuite1])
    return suite

# def testsuite1():
#     suite = group_testsuite
#     return suite

def testsum():
    suit1 = testsuite()
    # suit2 = testsuite1()
    suitlist = [suit1]
    suite = unittest.TestSuite(suitlist)
    return suite



if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestFromTestCase(Mydemo)
    # runner = unittest.TextTestRunner()
    # runner.run(testsuite())

