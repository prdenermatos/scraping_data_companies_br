from repository.elastic_db import ElasticsearchRepository as el

from cnaes.insert_cnaes import JSON_TO_INSERT_CNAE
from empresas.insert_empresas import JSON_TO_INSERT_EMPRESAS
from estabelecimento.insert_estabelecimento import JSON_TO_INSERT_ESTABELECIMENTO
from natureza.insert_natureza import JSON_TO_INSERT_NATUREZA

def insert_empresas() ->None:
    for i in JSON_TO_INSERT_EMPRESAS:
        el.insert_document(index='empresa', id=JSON_TO_INSERT_EMPRESAS[i]['CNPJ_BASICO'] , document=JSON_TO_INSERT_EMPRESAS[i])
        '''
        espera-se: 
            empresa: 1: {'CNPJ_BASICO': 41354981, 'RAZAO_SOCIAL': 'ROYAL COLLOR COMERCIO DE TINTAS LTDA', 'COD_NATU_JUR': 2062, 'COD_QUALIFICACAO': 49, 'CAPITAL_SOCIAL': 20000, 'COD_PORTE_EMPRESA': 3}            
        '''

def join_update_estabelecimento() -> None:
    empresa: list = el.find_all()
    for i in empresa:
        if (i['CNPJ_BASICO'] in JSON_TO_INSERT_ESTABELECIMENTO):
            el.insert_document(index='estabelecimento', id= f'{i}', document=JSON_TO_INSERT_ESTABELECIMENTO[i] )

    # find por CNPJ, se encontrado, insere update no objeto da empresa


def join_update_cnae_estabelecimento() -> None:
    for i in JSON_TO_INSERT_CNAE:
        el.find_document_by_id()
    # find por COD.CNAE no objeto de estabelecimento, se encontrado, insere fazendo uodate


def execute():
    insert_empresas()
    join_update_estabelecimento()
    join_update_cnae_estabelecimento()


execute()





