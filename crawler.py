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
    
    materiais = []
    precos = []
    datas = []
    for elemento in tabela('tr')[1:]:
        colunas = elemento('td')
        
        materiais.append(colunas[0].text)
        precos.append(colunas[2].text)
        datas.append(colunas[3].text)
        
    # salva em um data frame
    d = {
        'Material': materiais,
        'Preço': precos, 
        'Data': datas     
    }
    df = pd.DataFrame(d, index=['1', '2', '3', '4', '5', '6'])

    #exportar para o excel
    data_txt = date.today().strftime('%d_%m_%Y')
    nome_arquivo = 'dados/' + commodity + '_' + data_txt + '.xlsx'
    df.to_excel(nome_arquivo)
    
    # retorna onde o arquivo foi salvo
    return nome_arquivo