
import pandas as pd
import os

path_planilhas = 'src/empresas'

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
            'RAZAO_SOCIAL': '',
            'COD_NATU_JUR': '',
            'COD_QUALIFICACAO': '',
            'CAPITAL_SOCIAL': '',
            'COD_PORTE_EMPRESA': '',
            'ENTE_FEDERATIVO': '',  
        }
        for i in data:            # inserir método de insert a cada iteração do for para reduzir consumo memória
            object_company = {
                'CNPJ_BASICO': i[0],
                'RAZAO_SOCIAL': i[1],
                'COD_NATU_JUR': i[2],
                'COD_QUALIFICACAO': i[3],
                'CAPITAL_SOCIAL': i[4],
                'COD_PORTE_EMPRESA': i[5],
                'ENTE_FEDERATIVO': i[6]
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

def create_JSON_to_insert(total_csv_empresas: int):
    JSON_ALL_COMPANIES = dict()
    index = 0
    data = list()
    data_clean = list()
    c = 0
    for i in range(total_csv_empresas):
        name_file = f'src/empresas/empresas{i+1}.csv'
        # c += 1 
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
JSON_TO_INSERT_EMPRESAS = create_JSON_to_insert(total_planilhas)



'''

Saída da função

{
1: {'CNPJ_BASICO': 41354981, 'RAZAO_SOCIAL': 'ROYAL COLLOR COMERCIO DE TINTAS LTDA', 'COD_NATU_JUR': 2062, 'COD_QUALIFICACAO': 49, 'CAPITAL_SOCIAL': 20000, 'COD_PORTE_EMPRESA': 3},
2: {'CNPJ_BASICO': 41354981, 'RAZAO_SOCIAL': 'ROYAL COLLOR COMERCIO DE TINTAS LTDA', 'COD_NATU_JUR': 2062, 'COD_QUALIFICACAO': 49, 'CAPITAL_SOCIAL': 20000, 'COD_PORTE_EMPRESA': 3},
3: {'CNPJ_BASICO': 41354982, 'RAZAO_SOCIAL': 'FELIPE NUNES 02133569022', 'COD_NATU_JUR': 2135, 'COD_QUALIFICACAO': 50, 'CAPITAL_SOCIAL': 5000, 'COD_PORTE_EMPRESA': 1}, 
4: {'CNPJ_BASICO': 41354981, 'RAZAO_SOCIAL': 'ROYAL COLLOR COMERCIO DE TINTAS LTDA', 'COD_NATU_JUR': 2062, 'COD_QUALIFICACAO': 49, 'CAPITAL_SOCIAL': 20000, 'COD_PORTE_EMPRESA': 3}, 
5: {'CNPJ_BASICO': 41354982, 'RAZAO_SOCIAL': 'FELIPE NUNES 02133569022', 'COD_NATU_JUR': 2135, 'COD_QUALIFICACAO': 50, 'CAPITAL_SOCIAL': 5000, 'COD_PORTE_EMPRESA': 1}, 
6: {'CNPJ_BASICO': 41354983, 'RAZAO_SOCIAL': 'WALESKA EMANNUELLY LINS DOS SANTOS 09569333430', 'COD_NATU_JUR': 2135, 'COD_QUALIFICACAO': 50, 'CAPITAL_SOCIAL': 1000, 'COD_PORTE_EMPRESA': 1}
}


'''
