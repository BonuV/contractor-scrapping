from dataclasses import dataclass
import psycopg2
import logging

@dataclass
class database_details:
      host: str
      port: int
      username:str
      password: str
      database_name: str


class ConnectDB:
    '''Context manager class to connect to 
    postgress database'''
    def __init__(self,db_hostname,db_port,
                db_username,db_password , db_name):
        self.__logger=logging.getLogger("db_connect")
        self.rows=[]
        self._db_info=database_details(host=db_hostname,port=db_port,
                                username=db_username,password=db_password,
                                database_name=db_name)
    
    def __enter__(self):
        self.__database_conn=psycopg2.connect(host=self._db_info.host,
                        port=self._db_info.port,
                        database=self._db_info.database_name,
                        user=self._db_info.username,
                        password=self._db_info.password)
        self.__logger.info("connected to database {}".format(self._db_info.database_name))
        return self.__database_conn
    
    def __exit__(self,exc_type, exc_value, exc_tb):
        self.__database_conn.close()
        self.__logger.info("database connection to {} is closed".format(self._db_info.database_name))
        if exc_type is not None:
            print(self.rows)
            self.__logger.error("database closed with error {}".format(exc_value))