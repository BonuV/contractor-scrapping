from dbops import DBOperations
from dwnldinfo import dwnldConDetails
from dbconnect import ConnectDB
import sys
import logging
import os
import yaml


class extractconinfo:
    def __init__(self,state:-> str,query_file:->str):
        self.__state=state
        self.__query_file=query_file
        if self.__state is None:
            raise ValueError("please provide the state value to extract the info")
        self.__logger=logging.getLogger("extractcontractor_info")
        self.__logger.debug("state requested for is {}".format(self.__state))
    
    def loadup_data(self):
        latest_file_name=dwnldConDetails(self.__state)
        if latest_file_name==True:
            with open('resource.yml','rt') as resource_info:
                input_values=yaml.safe_load(resource_info)
                query_name=total_resources['STATE'][self._state][0]['query']
                dest_table=total_resources['STATE'][self._state][0]['table_to_upload']
                db_ops=DBOperations(self.__build_db_dict)
                db_ops.upload(latest_file_name, self.__query_file, query)



    def __build_db_dict(self):
        db_dtls={
            'db_hostname': os.environ('DB_HOST'),
            'db_port': os.environ('DB_PORT'),
            'db_username': os.environ('POSTGRES_USER'),
            'db_password': os.environ('POSTGRES_PASSWORD'), 
            'db_name': os.environ('POSTGRES_NAME')
        }
        return db_dtls



if __name__='main':
    state=sys.argv[1]
    extractconinfo
