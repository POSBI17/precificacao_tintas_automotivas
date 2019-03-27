# bibliotecas a serem utilizadas
from datetime import date
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd

def crawler_commodity(commodity):
    # prepara a url
    supported_commodities = {
        'methanol': {
            'id': '856',
            'type': 'Energy'
        },
        'propyleno': {
            'id': '438',
            'type': 'Chemical'
        },
        'ethylenene': {
            'id': '856',
            'type': 'Chemical'
        },
        'xylene': {
            'id': '1222',
            'type': 'Chemical'
        },
        'benzene': {
            'id': '120',
            'type': 'Chemical'            
        },
        'urea': {
            'id': '89',
            'type': 'chemical'
        },
        'polysilicon': {
            'id': '463',
            'type': 'chemical'
        },
        'styrene': {
            'id': '168',
            'type': 'chemical'
        },
        'toluene': {
            'id': '177',
            'type': 'chemical'
        },
        'acetic_acid': {
            'id': '218',
            'type': 'chemical'
        },
        'pa': {
            'id': '541',
            'type': 'chemical'
        },
        'acrylic_acid': {
            'id': '584',
            'type': 'chemical'
        },
        'titanium_dioxide': {
            'id': '645',
            'type': 'chemical'
        },
        'maleic_anhydride': {
            'id': '660',
            'type': 'chemical'
        },
        'nitric_acid': {
            'id': '723',
            'type': 'chemical'
        }
    }
    
    if (commodity not in supported_commodities):
        return ''

    url = 'http://sunsirs.com/uk/prodetail-' + supported_commodities[commodity]['id'] + '.html'
    
    # recupera o html
    get = urlopen(url)
    html = get.read()
    
    # Filtra o conteudo
    bsObj = BeautifulSoup(html, "html.parser")
    tabela = bsObj('table')[0]
    dados = [elemento.text for elemento in tabela('td')[4:] if elemento.text != supported_commodities[commodity]['type']]
    
    # salva em um data frame
    df = pd.DataFrame(dados)
    d = {
        'Material': [dados[0], dados[3], dados[6], dados[9], dados[12], dados[15]],
        'Preço': [dados[1], dados[4], dados[7], dados[10], dados[13], dados[16]], 
        'Data': [dados[2], dados[5],dados[8], dados[11], dados[14], dados[17]]     
    }
    df = pd.DataFrame(d, index=['1', '2', '3', '4', '5', '6'])
    
    #exportar para o excel
    data_txt = date.today().strftime('%d_%m_%Y')
    nome_arquivo = 'dados/' + commodity + '_' + data_txt + '.xlsx'
    df.to_excel(nome_arquivo)
    
    # retorna onde o arquivo foi salvo
    return nome_arquivo