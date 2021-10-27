import logging
import yaml
from dbconnect import ConnectDB

class DBOperations:
    def __init__(self,conn_details :-> dict):
        self.__db_hostname = conn_details['hostname']
        self.__db_port=conn_details['port']
        self.__db_username=conn_details['username']
        self.__db_password=conn_details['password']
        self.__db_name=conn_details['name']
        if self.conn_dtls is None:
            raise ValueError('connection details are not provided')
        self.__logger=logging.getLogger('dbOps')
    
    def upload(self,input_file,file_name,query_name):
        #define a db connection object
        with ConnectDB(self.__db_hostname,self.__db_port,self.__db_username,self.__db_password,self.__db_name) as conn:
            self.__logger._db_info('connected to the db {}',self.__db_name)
            #define a db cursor
            cursor=conn.cursor()
            #read the data file in chunks
            czine=1000 # no of records should get published
            for chunk in pd.read_csv(input_file,chunksize=csize):
                #replace the null values as ''
                chunk.fillna('',inplace=True)
                cols = ','.join(list(chunk.columns))
                #convert the data format of the columns to a standard format
                chunk['issued_date']=chunk['issued_date'].apply(convert_time)
                chunk['expiration_date']=chunk['expiration_date'].apply(convert_time)
                #change the records into tuples
                tuple_records = [tuple(x) for x in chunk.to_numpy()]
                #read the query from the file
                query_statement= self.__import_query(file_name, query_name)
                self.__logger.info('retrived the query string for {}', query_name)
                cursor.executemany(query_statement,tuple_records)
                self.__logger.info('uploaded  {} records into database', len(chunk))
                conn.commit()
    
    def __import_query(self,file_name, query_name):
        with open(file_name,'rt') as query_file:
            queries=yaml.safe_load(query_file.read())
            return queries[query_name]['query']

    def __convert_time(self,time):
        #convert the time values in YY-MONTH-DATE format 
        d1=time
        if d1!='':
            m=datetime.strptime(d1,'%d/%m/%y')
            return datetime.strftime(m,'%Y-%m-%d')
