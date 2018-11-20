from common.oracle import Oracle
from config.readconfig import db_url

oracle = Oracle(db_url)
case_debug = oracle.select("SELECT XF_CASEID FROM XF_CASEDEBUG")
print(case_debug)

mixid_list = oracle.dict_fetchall("select xf_mixid from xf_casedebug where xf_executeuser = '' order by xf_mixid")
print(mixid_list)