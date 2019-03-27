# Artigo POS BI 17

## Softwares
* Anaconda, uma plataforma que visa prover e gerenciar as dependecias de python e r do seu projeto, [instalação](https://www.anaconda.com/distribution/); 
* Project Jupyter, Um projeto open source que permite criar e compartilhar códigos e documentos, [instruções para instalação](https://jupyter.org/install);
* Python 3.3, linguagem de programação, está sendo utilizada para extração de dados, usando técnicas de web mining, [download](https://www.python.org/downloads/);

## Dados
* Dados de Commodities como: Acetic Acid, Acrylic Acid, Maleic_anhydride, nitric_acid, pa, polysilicon, styrene, titanium Dioxide, toluene, urea, Methanol, Benzene, Ethylene oxide, Propylene oxide e Xylene, retirados do [SunSirs Commodity data Group](http://sunsirs.com/) um site chines qe possue essas informações desse indice. 
* Dados da conversão da moeda chinesa(CNY) para brasileira(BRL) foi retirado do site [Exchange Rates UK](https://pt.exchangerates.org.uk/).

---

## Instalação do projeto

Todas as depedencias do projeto serão instaladas aqui.

### Windows 10
1. Baixe o Jupyter do python 3.7 para a sua distribuição de Windows 10, [clicando aqui](https://www.anaconda.com/distribution/), isso já fara com que o python e o jupyter sejam instalados; 
2. Realize o clone do projeto na pasta de seu usuario no computador;
3. Na barra de pesquisa do windows, digite *cmd* para abrir o terminal de comandos;
4. No terminal execute *jupyter notebook* para que o notebook abra;

### Ubuntu
1. Acesse o [link de download do anaconda](https://www.anaconda.com/distribution/) e faça o download referente a sua versão de sistema operacional;
2. Rode o arquivo que foi baixado através do comando *bash*;
3. Uma vez terminada a instalação, recarregue as configurações do seu terminal através do comando *source ~/.bashrc*;
4. Realize o clone do projeto no diretório desejado do seu computador;
4. Utilize cd para navegar no terminal até a pasta do projeto e então rodar o comando *jupyter notebook* para abrir o jupyter no diretório do projeto;

---

## Utilizando os dados:
**Obs. Para os commodities, devido ao site não possuir um histórico extenso, é necessário executar o código a cada 6 dias, por um batch ou manualmente. Para o dolar é necessario executar uma vez por ano.**

1. Realize os passos de instalação para o seu sistema operacional
2. Caso você deseje atualizar os dados:
    * Para as commodities, rode através do jupyter o script main na pasta de dados dados, isso irá gerar um novo excel contendo as informações das commodities da ultima semana;
    * Para o dolar, rode através do jupyter o script na pasta de dados chamado CNY_BRL.ipynb;

