
import pandas as pd
import os

path_planilhas = 'src/cnaes'

class DataManipulationCompanies:
    '''
    Possui a lógia de leitura e manipulação para uma planilha
    '''
    def __init__(self, CSV_PATH: str) -> None:
        self.csv_name = CSV_PATH
          
    def read_file_data_frame(self) -> pd.DataFrame:
        file = pd.read_csv(self.csv_name,  encoding= 'unicode_escape', sep=";", header = None)
        data_frame = pd.DataFrame(file)
        return data_frame 

    def set_data_dict_to_list(self, data) -> list:
        data_dict: dict =  data.to_dict('split')
        return data_dict['data']

    def constructor_json_list(self, data: list) -> list():
        list_json = list()
        object_company = {
            'CODIGO': '',
            'DESCRICAO': '',
   
        }
        for i in data:
            object_company = {
                'CODIGO': i[0],
                'DESCRICAO': i[1],
            }
            list_json.append(object_company)     
        return list_json
    

    def run(self):
        data_frame = self.read_file_data_frame()
        data_clean_list = self.set_data_dict_to_list(data_frame)
        json_list_to_insert_db = self.constructor_json_list(data_clean_list)
        return json_list_to_insert_db
 



def len_plans(path_name: str):
    files = []
    path = path_name
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return len(files) -1

def create_JSON_to_insert(total_csv: int):
    JSON_ALL_COMPANIES = dict()
    index = 0
    data = list()
    data_clean = list()
    for i in range(total_csv):
        name_file = 'src/cnaes/cnae.csv' 
        companies = DataManipulationCompanies(name_file)
        data.append(companies.run())
    for plan in data:
        for i in plan:
            data_clean.append(i)

    for record in data_clean:
        index += 1
        JSON_ALL_COMPANIES[index] = record

    print(JSON_ALL_COMPANIES)
    return JSON_ALL_COMPANIES



total_planilhas = len_plans(path_planilhas)
JSON_TO_INSERT_CNAE = create_JSON_to_insert(total_planilhas)



