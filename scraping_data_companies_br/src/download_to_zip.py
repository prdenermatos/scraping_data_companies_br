# from logging.config import dictConfig
# import wget
# from zipfile import ZipFile
# import os
# import pandas as pd


# def create_object_params(qtde_zip_companies: int) -> list():
#     param_list = list()
#     for i in range(qtde_zip_companies):
#         data_params = dict()
#         data_params['ZIPFILENAME'] = f'Empresas{i}.zip'
#         data_params['URLFILEDOWNLOAD'] = f'http://200.152.38.155/CNPJ/Empresas{i}.zip'
#         param_list.append(data_params)
#     return param_list

# param_companies_download = create_object_params(10) # é usado na chamada do run


# class DataManipulationCompanies:
#     def __init__(self, ZIPFILENAME: str, URLFILEDOWNLOAD: str) -> None:
#         self.zip_name = ZIPFILENAME
#         self.csv_name = ''
#         self.url_download = URLFILEDOWNLOAD
        
#     def download_extractor_cnaes(self) -> None:
#         wget.download(self.url_download, self.zip_name)
#         with ZipFile(self.zip_name, 'r') as zip:
#             zip.extractall()
#             self.csv_name = zip.namelist() # Para a tabela EMPRESAS contagem dinâmica
          
#     def read_file_data_frame(self) -> pd.DataFrame:
#         file = pd.read_csv(self.csv_name,  encoding= 'unicode_escape', sep=";")
#         data_frame = pd.DataFrame(file)
#         return data_frame 

#     def set_data_dict_to_list(self, data) -> list:
#         data.dropna(inplace = True)
#         data_dict: dict =  data.to_dict('split')   
#         return data_dict['data']

#     def constructor_json_list(self, data: list) -> list():
#         list_json = list()
#         object_company = {
#             'CNPJ_BASICO': '',
#             'RAZAO_SOCIAL': '',
#             'COD_NATU_JUR': '',
#             'COD_QUALIFICACAO': '',
#             'CAPITAL_SOCIAL': '',
#             'COD_PORTE_EMPRESA': '',
#             'ENTE_FEDERATIVO': '',
#         }
#         for i in range(len(self.csv_name)):
#             object_company['CNPJ_BASICO'] = data[0][0]
#             object_company['RAZAO_SOCIAL'] = data[0][1]
#             object_company['COD_NATU_JUR'] = data[0][2]
#             object_company['COD_QUALIFICACAO'] = data[0][3]
#             object_company['CAPITAL_SOCIAL'] = data[0][4]
#             object_company['COD_PORTE_EMPRESA'] = data[0][5]
#             object_company['ENTE_FEDERATIVO'] = data[0][6]
#             list_json.append(object_company)
#         return object_company
    
#     def insert_db(json: list) -> None:
#         ''' lógica importar da class do elastic'''


#     def run(self):
#         if (os.path.isfile(self.zip_name)):
#             os.remove(self.zip_name)
#         if (os.path.isfile( self.csv_name)):
#             os.remove( self.csv_name)
#         self.download_extractor_cnaes()
#         data_frame = self.read_file_data_frame()
#         data_clean_list = self.set_data_dict_to_list(data_frame)
#         json_list_to_insert_db = self.constructor_json_list(data_clean_list)
#         self.insert_db(json_list_to_insert_db)
#         os.remove(self.zip_name)
#         os.remove( self.csv_name)



# def data_insert_all(param_companies: list):
#     for i in param_companies:
#         companies = DataManipulationCompanies(i['ZIPFILENAME'], i['URLFILEDOWNLOAD'])
#         companies.run()

# data_insert_all(param_companies_download)



