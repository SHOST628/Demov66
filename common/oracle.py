import cx_Oracle


class Oracle:
    def __init__(self,db_url):
        """db_url: the path of connection
            db_url  eg: PROMOTION/PROMOTION@172.31.6.234:1521/TESTDB
        """

        self._conn = cx_Oracle.connect(db_url)
        self._cursor = self._conn.cursor()

    def select(self,db_url,sql):
        pass

    def dict_fetchall(self,sql):
        """Return all rows from a cursor as a dict"""
        try:
            self._cursor.execute(sql)
            columns = [col[0] for col in self._cursor.description]
            return [
                dict(zip(columns, row))
                for row in self._cursor.fetchall()
            ]
        except Exception as e:
            raise e

    # def select_all(self,db_url,sql_string):
    #     conn = cx_Oracle.connect(db_url)
    #     cusor = conn.cusor()
    #     cusor.excute(sql_string)
    #     cusor.fetchall()

    def select_many(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def close(self):
        self._cursor.close()
        self._conn.close()