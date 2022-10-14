
import pandas as pd
import os

path_planilhas = 'src/estabelecimento'

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
            'CNPJ_BASICO': '',
            'CNPJ_ORDEM': '',
            'CNPJ_DV': '',
            'IDENTIFICADOR': '',
            'NOME_FANTASIA': '',
            'COD_SITUACAO': '',
            'DT_SITUACAO': '',
            'COD_MOTIVO': '',
            'NOME_CIDADE_EXTERIOR': '',
            'COD_PAIS': '', 
            'DT_INICIO': '', 
            'COD_CNAE_PRINCIPAL': '',
            'COD_CNAE_SECUNDARIO': '', 
            'TIPO_LOGRADOURO': '',
            'NOME_LOGRADOURO': '',
            'NRO_LOGRADOURO': '',
            'COMP_LOGRADOURO': '', 
            'BAIRRO': '',
            'CEP': '', 
            'UF': '', 
            'COD_MUNICIPIO': '',
            'DDD_1': '',
            'TELEFONE_1': '',
            'DDD_2': '',
            'TELEFONE_2': '',
            'DDD_FAX': '',
            'TELEFONE_FAX': '',
            'EMAIL': '',
            'SITUACAO_ESPECIAL': '',
            'DT_SITUACAO_ESPECIAL': '',


   
        }
        for i in data:
            object_company = {
                'CNPJ_BASICO': i[0],
                'CNPJ_ORDEM': i[1],
                'CNPJ_DV': i[2],
                'IDENTIFICADOR': i[3],
                'NOME_FANTASIA': i[4],
                'COD_SITUACAO': i[5],
                'DT_SITUACAO': i[6],
                'COD_MOTIVO': i[7],
                'NOME_CIDADE_EXTERIOR': i[8],
                'COD_PAIS': i[9], 
                'DT_INICIO': i[10], 
                'COD_CNAE_PRINCIPAL': i[11],
                'COD_CNAE_SECUNDARIO': i[12], 
                'TIPO_LOGRADOURO': i[13],
                'NOME_LOGRADOURO': i[14],
                'NRO_LOGRADOURO': i[15],
                'COMP_LOGRADOURO': i[16], 
                'BAIRRO': i[17],
                'CEP': i[18], 
                'UF': i[19], 
                'COD_MUNICIPIO': i[20],
                'DDD_1': i[21],
                'TELEFONE_1': i[22],
                'DDD_2': i[23],
                'TELEFONE_2': i[24],
                'DDD_FAX': i[25],
                'TELEFONE_FAX': i[26],
                'EMAIL': i[27],
                'SITUACAO_ESPECIAL': i[28],
                'DT_SITUACAO_ESPECIAL': i[29],
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
        name_file = f'src/estabelecimento/estabelecimento{i+1}.csv'    
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
JSON_TO_INSERT_ESTABELECIMENTO = create_JSON_to_insert(total_planilhas)



