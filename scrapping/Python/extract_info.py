import requests
import json
from resource import resourceUrl
from dbops import DBOperations

class nashvilleContractors:
    def __init__(self,state,name->None):
        self.state=state
        self.name=name
    
    def extract_info(self):
        id_params={'name':self.name}
        response=requests.get(self.url,params=id_params)
        con_type_json=json.loads(response.content)
        con_type_id=con_type_json[0]['id']

        if con_type_id is not None:
            #once after extracting the contractor type id
            #extract the data belonging to the id
            file_url=self.url+con_type_id+"/"+"rows.csv"
            file_params={'accessType':'DOWNLOAD'}
            response=requests.get(file_url,params=id_params)        
            page_content=response.content

            #once the content is copied , dump the bytes data into a csv file
            with open('../data/nashville_contractors.csv','wb') as extract_file:
                data_file=extract_file.write(page_content)
        else:
            raise ValueError("couldn't find the id for provided name")
    
    def upload_contractors(self);
        DBOperations()
        








    

