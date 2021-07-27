## TCC - Rodrigo da Silva de Almeida
TCC Puc Minas - Agosto de 2021

APLICAÇÃO DE MODELOS DE MACHINE LEARNING PARA ANÁLISE DE DEMONSTRAÇÕES CONTÁBEIS E CLASSIFICAÇÃO DE EMPRESAS PARA INVESTIMENTO NO LONGO PRAZO.

### Instruções:

O arquivo **TCC_PucMinas_VersaoFinal.ipynb** contém o notebook desenvolvido no TCC, que pode ser executado no Jupyter Notebook do Anaconda. O notebook carrega os dados coletados no sítio da Bolsa de Valores Mobiliários (CVM) faz os tratamentos e a devida exploração dos dados, executa os algoritmos de aprendizado de máquina, apresenta a análise dos resultados, e, no final, gera a base de dados e salva o modelo em disco para posterior utilização (arquivos disponíveis na pasta **Base de Dados e Classificador**). Este notebook também utiliza o arquivo **df_cvm.xlsx**.

O notebook **Carregar um classificador treinado.ipynb** carrega a base de dados criada no notebook acima citado, aplica o modelo e faz a predição do resultado.

O arquivo **app-tcc.py** foi desenvolvido no editor de texto *Visual Studio Code* e com o auxílio da biblioteca *streamlit* foi possível criar um aplicativo web para exibir a solução de Machine Learning para o problema proposto. Este arquivo utiliza os arquivos disponíveis na pasta **Base de Dados e Classificador**.

O notebook **Retorno Carteira.ipynb** trata da análise de uma carteira de investimento, com a seleção de algumas empresas classificadas como "boa". Este notebook faz uso dos arquivos **bases_classificacao.pkl** disponível na pasta **Base de Dados e Classificador** e do arquivo **carteira_acoes1.xlsx**.

### Observação:
Não foi possível carregar os arquivos da pasta ZIP já descompactados e nem os arquivos consolidados por exercício, devido às limitações do repositório em quantidade e tamanho do arquivo.
No entanto, é possível obtê-los com a execução do notebook **TCC_PucMinas_VersaoFinal.ipynb**.
Os demais arquivos gerados e utilizados no projeto estão disponíveis para consulta nas pastas correspondentes deste repositório.
