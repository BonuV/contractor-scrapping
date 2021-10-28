import requests
import json
import logging
#from resource import resourceUrl
import yaml
#from dbops import DBOperations

class dwnldConDetails:
    def __init__(self,state):
        self.__state=state
        if self.__state is None:
            raise ValueError('state is a mandatory value')
        self.__logger=logging.getLogger("__extractor-contractorinfo__")
        self.__logger.info("state provided is {}".format(self.__state))
        
        if self.__state=='TN':
            self.nashville_contractors()
        elif self.__state=='AZ':
            self.arizona_contractors()
        
    
    def nashville_contractors(self):
        '''method to download the nashville contractors from api based on
         the contractor type'''
        with open('resource.yml','rt') as input_data:
              total_resources=yaml.safe_load(input_data)
              url=total_resources['STATE'][self.__state][0]['Resource_point']
              name=total_resources['STATE'][self.__state][0]['name']
        self.__logger.debug("api point for state {}  is {}".format(self.__state,url))

        id_params={'name':name}
        response=requests.get(url,params=id_params)
        con_type_json=json.loads(response.content)
        con_type_id=con_type_json[0]['id']
        self.__logger.info("id for the contractor type {} is {}".format(name,con_type_id))

        if con_type_id is not None:
            #once after extracting the contractor type id
            #extract the data belonging to the id
            file_url=url+'/'+con_type_id+"/"+"rows.csv"
            file_params={'accessType':'DOWNLOAD'}
            self.__logger.info("file to be downloaded {}".format(file_url))
            response=requests.get(file_url,params=id_params)        
            page_content=response.content

            #once the content is copied , dump the bytes data into a csv file
            with open('../Postgres/data/nashville_contractors.csv','wb+') as extract_file:
                data_file=extract_file.write(page_content)
            return extract_file.name
        else:
            self.__logger.error("couldn't find the id for the provided name")
            raise ValueError("couldn't find the id for provided name {}".format(name))        
    
    def arizona_contractors(self):
        with open('resource.yml','rt') as input_data:
            total_resources=yaml.safe_load(input_data)
            file_url=total_resources['STATE'][self.__state][0]['Resource_point']
            self.__logger.info('url provided {}'.format(file_url))

            self.__logger.info("file to be downloaded {}".format(file_url))
            response=requests.get(file_url)
            if response.status_code==200:      
                page_content=response.content

                #once the content is copied , dump the bytes data into a csv file
                with open('../Postgres/data/arizona_contractors.csv','wb+') as extract_file:
                    data_file=extract_file.write(page_content)
                return extract_file.name
            else:
                self.__logger.error("facing error with resource url")
                raise ValueError("couldn't find the provided resource {} ".format(url))







    

