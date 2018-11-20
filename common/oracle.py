import cx_Oracle
from cx_Oracle import ProgrammingError
from common.logger import logger


class Oracle:
    def __init__(self,db_url):
        """db_url: connection path format
            db_url  eg: PROMOTION/PROMOTION@172.31.6.234:1521/TESTDB
        """
        self._conn = cx_Oracle.connect(db_url)
        self._cursor = self._conn.cursor()

    def dict_fetchall(self,sql):
        """Return all rows from a cursor as a dict"""
        try:
            self._cursor.execute(sql)
            columns = [col[0] for col in self._cursor.description]
            return [
                dict(zip(columns, row))
                for row in self._cursor.fetchall()
            ]
        except ProgrammingError as e:
            logger.exception(e)
            raise e

    def select(self,sql):
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
            return result
        except ProgrammingError as e:
            logger.exception(e)
            raise e

    def insert(self):
        pass

    def update(self):
        pass

    def close(self):
        self._cursor.close()
        self._conn.close()