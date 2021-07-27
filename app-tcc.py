import pandas as pd
import streamlit as st
import pickle

# Carregando dataset_original
dataset = pd.read_excel('D:/Puc Minas/Projeto/TCC/dataset_original.xlsx')

# Carregando o Modelo Treinado
rede_neural = pickle.load(open('D:/Puc Minas/Projeto/TCC/rede_neural_finalizado.sav', 'rb'))

# Carregando a Base de dados
registros = pickle.load(open('D:/Puc Minas/Projeto/TCC/bases_classificacao.pkl', 'rb'))

# título
st.title("App - Classificação e Análise de Demonstrações Contábeis")

# subtítulo
st.markdown("Este é um App utilizado para exibir a solução de Machine Learning para o problema de classificação de demonstrações financeiras de empresas listadas na Bolsa de Valores.")

# Título da barra lateral
st.sidebar.subheader("Defina os atributos da empresa para classificação")

# Selecionando os nomes das empresas
empresa = registros[1][['DENOM_CIA']].sort_values(['DENOM_CIA']).drop_duplicates()

# Criando uma caixa de seleção para o nome das empresas e apresenrando como título
empresa_choice = st.sidebar.selectbox('Escolha a empresa', empresa)
st.header('Empresa: ' + empresa_choice.upper())

# Buscando o exercício de acordo com a empresa selecionada e apresentando numa caixa de seleção
exercicio = dataset[dataset['DENOM_CIA'] == empresa_choice][['DT_FIM_EXERC']].sort_values(['DT_FIM_EXERC']).drop_duplicates()
exerc_choice = st.sidebar.selectbox('Escolha o Período', exercicio)

# Buscando o ticker da empresa selecionada
ticker = dataset[dataset['DENOM_CIA'] == empresa_choice][['ticker']].drop_duplicates()
ticker = str(ticker)[-6:]
st.write('Ticker: ', ticker)

# Buscando o setor econômico da empresa selecionada
setor = dataset[dataset['DENOM_CIA'] == empresa_choice][['SETOR ECONÔMICO']].drop_duplicates()
setor = str(setor).replace('SETOR ECONÔMICO', '').rsplit()[1:]
setor = ' '.join(setor)
st.write('Setor Econômico: ', setor)

# Apresenta o indicadores de acordo com a empresa e o ano selecionado
indices = dataset[(dataset['DENOM_CIA'] == empresa_choice) & (dataset['DT_FIM_EXERC'] == exerc_choice)]
indices = indices.iloc[:, 6:-1]
st.write('Indicadores: ', indices)

# SELECIONANDO O REGISTRO PARA SER APLICADO O MODELO

# Seleciona o index dos dados selecionados
selecao_index = dataset[(dataset['DENOM_CIA'] == empresa_choice) & (dataset['DT_FIM_EXERC'] == exerc_choice)]
selecao_index = int(selecao_index.index.values)

# Seleciona a Variável independente "X" de acordo com o index acima
variavelX = registros[2][selecao_index]

# Convertendo em Matriz
variavelX = variavelX.reshape(1, -1)

# APLICANDO O MODELO DE REDE NEURAL
resultado = rede_neural.predict(variavelX)

# Fazendo um tratamento para aparecer bom ou ruim em vez de 0 ou 1.
if resultado == 0:
    result = 'Ruim'
else:
    result = 'Bom'

# Criando uma caixa de texto e apresentando o resultado da classificação
st.header('Resultado')
st.write('Balanço classificado como: ', result)
