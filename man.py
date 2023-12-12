import pandas as pd 

data = {'Nome': ['ADRIANO', 'RODRIGO', 'JULIANO', 'MATEUS', 'LUIZA', 'RODRIGO', 'RAYAN', 'FABIANO'],
        'Sobronome': ['SOARES', 'TADEWALD', 'FACCIONI', 'KIENZLE', 'CHEROBINI', 'VASCONCELLOS', 'DAVID', 'ARAUJO'],
        'Idade': [20, 30, 40, 18 ,25, 23, 15,45]}
    
df= pd.DataFrame(data)
#selcionando colunas
df.columns
df['Nome']
#selicionando mais de uma coluna
df[['Nome', 'Idade']]
#excluindo uma coluna do dataframe
colunas = [col for col in df.columns if not col in ['Sobronome']]

#filtrando por indexação(.iloc)
df.iloc[1:3] #pegando da 1 linha ate a 3
df.iloc[2:, 0] #pegando da 2 linha e so a 1 coluna 

#filtrando por condição (.loc)
df.loc[df['Nome']=='rayan']

df.loc[(df['Nome']=='rayan') & (df['Idade'] < 28)]
df.loc[(df['Nome']=='rayan') | (df['Idade'] < 28)]

#ADICIONANDO NOVAS COLUNAS
df['ENDERECO']= ['ASA NORTE ', 'ASA SUL', 'GAMA', 'GOIANIA', 'EUA', 
                 'BRAZLANDIA', 'CEILANDIA', 'GUARA']

#USANDO O METODO INSERT
df.insert(3,'PAIS',['BRASIL', 'AFRICA', 'CANADA', 'EUA', 'JALAPAO', 'JAPAO', 'MEXICO', 'BUENOS ARIES'])

#CRIANDO COLUNA A PARTIR DE SERIES
df['DOBRO DA IDADE'] = df['Idade'] * 2

#ADICIONANDO LINHAS
df.loc[len(df)] = ['ROBERTA', 'DE SOUZA', 26]