from common.oracle import Oracle
from config import readconfig
from common.logger import logger


oracle = Oracle(readconfig.db_url)
Flag = readconfig.debug_mode

# deciding execute all testcases or debug some testcases controling by the config mode in ini,if mode == 1,
# debug case,else execute all testcases
# the config executeuser deciding whose testcase to execute
if Flag:
    logger.info("***调试模式***")
    execute_user = readconfig.execute_user
    if execute_user == '':
        sql = "select xf_caseid from xf_casedebug where xf_executeuser is null " \
              "and xf_caseid is not null order by xf_caseid"
        testcaseid_list = oracle.dict_fetchall(sql)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser is null " \
              "and xf_mixid is not null order by xf_mixid"
        mixid_list = oracle.dict_fetchall(sql)
    else:
        sql = "select xf_caseid from xf_casedebug where xf_executeuser = '%s' " \
              "and xf_caseid is not null order by xf_caseid" % execute_user
        testcaseid_list = oracle.dict_fetchall(sql)
        sql = "select xf_mixid from xf_casedebug where xf_executeuser = '%s' " \
              "and xf_mixid is not null order by xf_mixid" % execute_user
        mixid_list = oracle.dict_fetchall(sql)
    mixcase_list = []
    for i in mixid_list:
        mixid = i["XF_MIXID"]
        sql = "select * from xf_mixcase where xf_mixid = '%s'" % mixid
        mixcase_list = mixcase_list + oracle.dict_fetchall(sql)
else:
    logger.info("***普通模式***")
    sql = "select distinct xf_caseid from xf_testcase"
    testcaseid_list = oracle.dict_fetchall(sql)
    sql = "select * from xf_mixcase"
    mixcase_list = oracle.dict_fetchall(sql)
    sql = "select xf_mixid from xf_mixcase"
    mixid_list = oracle.dict_fetchall(sql)

oracle.close()