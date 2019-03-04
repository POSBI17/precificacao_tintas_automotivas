# Artigo POS BI 17

## Softwares
* Project Jupyter, Um projeto open source que permite criar e compartilhar códigos e documentos, Instruções para instalação: https://jupyter.org/install;
* Python, linguagem de programação, está sendo utilizada para extração de dados, usando técnicas de web mining, url para download: https://www.python.org/downloads/;

## Dados
* Dados de Commodities como: Acetic Acid, Acrylic Acid, Maleic_anhydride, nitric_acid, pa, polysilicon, styrene, titanium Dioxide, toluene, urea, Methanol, Benzene, Ethylene oxide, Propylene oxide e Xylene, retirados do http://sunsirs.com/ um site chines qe possue essas informações desse indice. 
*Dados da conversão da moeda chinesa(CNY) para brasileira(BRL) foi retirado do https://pt.exchangerates.org.uk/.

## Utilizando os dados:
1. Instale o python e o Jupyter;
2. Adicionar esta pasta ao workplace do jupyter;
3. Rodar os scripts python da pasta dados utilizando o jupyter;
4. Será salvo na pasta dados um arquivo excel com os dados ja tratados;
5. Para os commodities, devido ao site não possuir um histórico extenso, é necessário executar o código a cada 6 dias, por um batch ou manualmente.
6. Para a moeda, será necessário rodar apenas uma vez pois o site traz um histórico de 1 ano.
