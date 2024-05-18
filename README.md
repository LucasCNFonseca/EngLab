**Detecção de Fraudes em Transações Financeiras com Inteligência Artificial**

---

## Visão Geral

Este repositório contém uma aplicação de inteligência artificial (IA) desenvolvida para detectar fraudes em transações realizadas em instituições financeiras. A aplicação utiliza técnicas avançadas de aprendizado de máquina e processamento de dados para identificar padrões suspeitos e potenciais atividades fraudulentas em tempo real.

## Funcionalidades

- **Detecção de Anomalias**: Utiliza algoritmos de detecção de anomalias para identificar transações que se desviam significativamente do comportamento típico.
- **Classificação**: Classifica as transações como legítimas ou fraudulentas com base em modelos de aprendizado de máquina treinados com dados históricos.
- **Atualização Dinâmica**: Aperfeiçoa continuamente os modelos de IA com novos dados para melhorar a precisão da detecção de fraudes ao longo do tempo.
- **Interface Amigável**: Interface intuitiva para visualizar estatísticas, métricas de desempenho e resultados da detecção de fraudes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para o desenvolvimento da aplicação.
- **Flask**: Framework web utilizado para criar a interface de usuário da aplicação.
- **HTML/CSS/JavaScript**: Tecnologias front-end para o desenvolvimento da interface de usuário.

---

## Como Utilizar

Este projeto pode ser facilmente executado no ambiente do Google Colab, o que proporciona uma experiência de execução em um ambiente de notebook Python baseado na nuvem. Siga estas etapas para executar a aplicação:

1. **Abra o Notebook no Google Colab**: Clique no link abaixo para abrir o notebook no Google Colab:

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zI_jCpfAeQg8_bmVdgS0bh3zcg58RpMK?usp=sharing)

2. **Execute o Notebook**: Após abrir o notebook no Google Colab, clique em "Runtime" e depois em "Run all" para executar todas as células do notebook.

3. **Acesse a Interface**: Depois que todas as células forem executadas com sucesso, você poderá acessar a interface da aplicação. Siga as instruções fornecidas no notebook para acessar a interface e interagir com a aplicação.

4. **Utilize a Aplicação**: Explore as funcionalidades da aplicação, faça testes e experimente diferentes cenários para entender o funcionamento da detecção de fraudes em transações financeiras com inteligência artificial.

Utilizar o Google Colab proporciona uma maneira conveniente e gratuita de executar e interagir com o projeto sem a necessidade de configurar um ambiente de desenvolvimento local.

--- 

Você pode substituir "https://colab.research.google.com/drive/1zI_jCpfAeQg8_bmVdgS0bh3zcg58RpMK?usp=sharing" pelo link direto para o seu notebook hospedado no Google Colab.

## Descrição dos Requisitos do Sistema

1. Tipos de Entrada
- Dados de Transações: Dados de transações financeiras, incluindo detalhes como ID da transação, data e hora, valor, localização geográfica, ID do cliente, tipo de transação, entre outros.
- Etiquetas de Fraude: Informações de rotulagem indicando se uma transação foi identificada como fraudulenta ou não, com base em verificações manuais ou sistemas pré-existentes.
- Dados de Treinamento e Teste: Conjuntos de dados históricos utilizados para treinar e validar os modelos de detecção de fraudes.

2. Fluxo do Usuário
1. Autenticação e Autorização:
   - O usuário (geralmente um analista de fraude ou um administrador de TI) faz login no sistema utilizando credenciais seguras.
   - O sistema verifica as credenciais e autoriza o acesso com base no nível de permissão do usuário.
   
2. Carregamento de Dados:
   - O usuário carrega novos dados de transações através de uma interface web, utilizando arquivos CSV ou conexões de API com sistemas de transações existentes.
   - O sistema valida os dados, verificando formatos e consistência, e armazena os dados em um banco de dados seguro.

3. Treinamento do Modelo:
   - O usuário inicia o processo de treinamento do modelo de machine learning.
   - O sistema utiliza os dados de treinamento para construir e validar os modelos (árvore de decisão, SVM, regressão logística), exibindo métricas de performance (precisão, recall, F1-score) após o treinamento.

4. Detecção de Fraudes:
   - O usuário submete novos dados de transações para análise.
   - O sistema aplica os modelos treinados para prever a probabilidade de cada transação ser fraudulenta, retornando uma classificação (fraudulenta ou não) e uma pontuação de confiança.

5. Visualização de Resultados:
   - O usuário visualiza os resultados da detecção de fraudes através de dashboards interativos, que exibem detalhes das transações, estatísticas de fraudes e gráficos de análise.
   - Opções de filtragem e exportação de relatórios estão disponíveis para análise aprofundada e documentação.

3. Framework e Funcionamento

## Frontend:
- Framework: React.js para construir uma interface de usuário interativa e responsiva.
- Funcionalidades:
  - Formulários para upload de dados.
  - Dashboards para visualização de resultados.
  - Páginas de login e autenticação.

## Backend:
- Framework: Flask ou Django (Python) para construção de APIs RESTful.
- Funcionalidades:
  - Autenticação e autorização de usuários.
  - Endpoints para upload e validação de dados.
  - Módulos de treinamento e previsão de modelos de machine learning.
  - Armazenamento seguro e gerenciamento de dados transacionais.

## Modelos de Machine Learning:
- Linguagem: Python.
- Bibliotecas: 
-	import pandas as pd
-	import numpy as np
-	import matplotlib.pyplot as plt
-	from sklearn.model_selection import train_test_split
-	from sklearn.neighbors import KNeighborsClassifier
-	from sklearn import metrics
-	from sklearn.metrics import classification_report, confusion_matrix
-	import itertools
-	from sklearn.metrics import classification_report
-	from imblearn.combine import SMOTETomek
-	import seaborn as sns
-	import matplotlib.gridspec as gridspec
-	from sklearn.preprocessing import StandardScaler
-	from sklearn.linear_model import LogisticRegression
-	from sklearn.model_selection import KFold
-	from sklearn.metrics import recall_score
-	from sklearn.svm import SVC
-	from sklearn.metrics import accuracy_score, recall_score, precision_score
-	from sklearn.tree import DecisionTreeClassifier
-	from google.colab import drive
-	from google.colab import files
-	from sklearn.model_selection import GridSearchCV
-	import matplotlib.dates as mdates
-	from matplotlib.ticker import MaxNLocator
-	import matplotlib.ticker as mtick
-	import matplotlib.ticker as ticker
- Algoritmos: Árvores de Decisão, SVM, Regressão Logística.

4. Aplicações Backend e Endpoints

## Endpoints e Funcionamento:

1. Autenticação e Gerenciamento de Usuários:
   - `POST /api/login`: Autentica o usuário e retorna um token JWT.
   - `POST /api/register`: Registra um novo usuário no sistema.
   - `POST /api/logout`: Invalida o token do usuário.

2. Gerenciamento de Dados:
   - `POST /api/upload`: Recebe e valida dados de transações enviados pelo usuário. Armazena os dados no banco de dados.
   - `GET /api/transactions`: Retorna uma lista de transações armazenadas, com opções de filtragem.

3. Treinamento de Modelos:
   - `POST /api/train`: Inicia o processo de treinamento dos modelos de machine learning com os dados fornecidos.
   - `GET /api/models`: Retorna uma lista de modelos treinados e suas métricas de performance.

4. Previsão de Fraudes:
   - `POST /api/predict`: Recebe novos dados de transações e retorna as previsões de fraude feitas pelos modelos treinados.

5. Visualização e Relatórios:
   - `GET /api/dashboard`: Fornece dados e estatísticas para exibição nos dashboards de visualização de resultados.
   - `GET /api/reports`: Gera e retorna relatórios detalhados sobre a detecção de fraudes, com opções de exportação.

6. Como funcionam para o Usuário:
- O usuário interage com a interface web para fazer upload de dados, iniciar o treinamento de modelos e visualizar resultados.
- As interações da interface web são manejadas pelo backend através dos endpoints definidos.
- A segurança dos dados e a integridade das operações são asseguradas por autenticação robusta e validações rigorosas implementadas no backend.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/sua-feature`)
3. Faça commit de suas mudanças (`git commit -am 'Adicione uma nova feature'`)
4. Faça push para a branch (`git push origin feature/sua-feature`)
5. Envie um pull request

## Autores

- Lucas Henrique Silva Porto Moraes
- Lucas de Castro Nunes Fonseca 
- Laura Alves Silva
- Marlon José da Silva Tenório
- Nichollas Rocha de Araújo Paes 

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---
Este readme fornece uma visão geral e instruções básicas para o uso e contribuição para a aplicação de detecção de fraudes em transações financeiras utilizando inteligência artificial. Sinta-se à vontade para expandir ou personalizar conforme necessário.
