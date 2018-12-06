from pages.keywords.keyword import BaseKeyword
from common.logger import logger
from common.storage import Storage
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

    def send_file(self,loc,file_path):
        """
        upload file
        :param loc: the path of the input path
        :param file_path: file path
        :return: None
        """
        self.send_file(loc,file_path)

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
