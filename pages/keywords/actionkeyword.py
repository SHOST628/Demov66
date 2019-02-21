from pages.keywords.keyword import BaseKeyword
from common.logger import logger
from common.storage import Storage
from common.oracle import Oracle
from config import readconfig
import time
import re

class Action(BaseKeyword):
    def get_current_date(self,name = 'curtime'):
        """
        store time value
        :param name: variate name
        :return:
        """
        t = time.strftime('%Y-%m-%d',time.localtime())
        self._storage(name,t)

    def import_file(self, loc, file_name):
        """
        upload file
        :param loc: the path of the input path
        :param file_name: file path
        :return: None
        """
        self.upload_file(loc, file_name)

    def accept_prompt(self):
        # this is all prompt location in v66
        loc = "//div[@class='popupContent']/div/p"
        # loc = ""
        self.click(loc)

    # set variate
    def _storage(self,var,value):
        setattr(Storage,var,value)

    # store variate
    def storage_docno(self,var):
        loc = "//div[@class='popupContent']/div/p"
        contain_text = self.find_element(loc).text
        # get documnent no
        doc_no =''.join(re.findall("[A-Za-z0-9]",contain_text))
        # variate name
        setattr(Storage,var,doc_no)
        logger.info('存储单号为%s'%doc_no)
        self.accept_prompt()

    # locate menu tree
    def locate_menu_by_text(self,*text):
        loc = ""
        for t in text:
            loc = "//span[contains(text(),'%s')]" % t
            self.click(loc)

    # TODO to be fixed (can't use this keyword)
    def locate_menu_by_id(self,*location_ids):
        oracle = Oracle(readconfig.db_url)
        sql = ""
        for location_id in location_ids:
            sql = "select xf_location from xf_pagelocation where xf_locationid = '%s'" % location_id
            location_list = oracle.dict_fetchall(sql)
            location = location_list[0]['XF_LOCATION']
            if location == None:
                raise Exception("location_id 错误，无法找到对应的location")
            self.click(location)

    def assert_in_prompt(self,member,msg=None):
        text = self.get_text("//div[@class='popupContent']/div/p")
        assert member in text,'%s'%msg

    def testcase_doc(self,desci):
        logger.info("用例描述 ：%s" % desci)
