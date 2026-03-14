
<img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=30% height=30%>

# AI Project Document - FarmTech Solutions - Módulo 1 - FIAP

## Grupo 70

#### Integrantes do grupo
Caroline Coelho
Leandro Paiva
Lucas Viana
Matheus Lima


## Sumário

[1. Introdução](#c1)

[2. Visão Geral do Projeto](#c2)

[3. Desenvolvimento do Projeto](#c3)

[4. Resultados e Avaliações](#c4)

[5. Conclusões e Trabalhos Futuros](#c5)

[6. Referências](#c6)

[Anexos](#c7)

<br>

# <a name="c1"></a>1. Introdução

## 1.1. Escopo do Projeto

### 1.1.1. Contexto da Inteligência Artificial

A Inteligência Artificial (IA) se tornou uma das principais tecnologias em vários setores da economia, como saúde, indústria, finanças e agricultura. Na agricultura, a IA está ligada à Agricultura Digital, que usa dados, algoritmos e ferramentas para aumentar a eficiência na produção agrícola.

Esse campo envolve tecnologias como sensores, análise de dados e aprendizado de máquina, que ajudam os agricultores com o planejamento e manejo das lavouras. Com a IA, é possível otimizar o uso de fertilizantes, água e espaço, resultando em maior produtividade e redução de custos.

A agricultura digital é uma tendência global, especialmente em países com grande produção agrícola. No Brasil, essa tecnologia é significativa, dado o peso do agronegócio na economia. As soluções de IA são usadas para monitorar culturas, prever produtividade, analisar solo e gerenciar insumos.

Nesse cenário, as empresas de tecnologia agrícola, chamadas de AgTechs, desenvolvem ferramentas para ajudar os produtores a tomar decisões mais informadas.

### 1.1.2. Descrição da Solução Desenvolvida

A solução desenvolvida neste projeto é uma aplicação que simula um sistema de apoio à gestão agrícola, focada no planejamento de lavouras de milho e soja. Criada com a linguagem de programação Python, ela calcula a área de plantio, a quantidade de ruas de plantio, a estimativa de plantas e o manejo de fertilizantes.

A aplicação recebe informações sobre as dimensões do terreno e parâmetros agronômicos, como o espaçamento entre linhas e a dose de fertilizante. Com esses dados, o sistema calcula automaticamente indicadores importantes para o planejamento agrícola.

Além disso, esta solução utiliza a linguagem R para se conectar a uma API meteorológica pública. Assim, ela coleta dados climáticos, processa essas informações e exibe os resultados no terminal.

Os dados gerados pela aplicação são exportados para análise estatística na linguagem R, permitindo o cálculo de métricas como média e desvio padrão. Essa integração proporciona uma análise mais profunda das informações, melhorando a compreensão dos dados da lavoura.

A solução traz valor ao cliente ao organizar melhor as informações da produção agrícola, facilitando a tomada de decisões sobre o manejo das culturas e o uso eficiente de insumos.

# <a name="c2"></a>2. Visão Geral do Projeto

## 2.1. Objetivos do Projeto

O principal objetivo deste projeto é desenvolver uma aplicação que ajude no planejamento e gestão das lavouras utilizando a agricultura digital.

## 2.2. Público-Alvo

O público-alvo da solução inclui profissionais e organizações do setor agrícola, como produtores rurais, técnicos agrícolas, engenheiros agrônomos e empresas de tecnologia agrícola.

Esses usuários podem usar sistemas semelhantes para planejar o plantio, estimar insumos e analisar dados de produção. A solução também pode ser útil em ambientes educacionais, como cursos de tecnologia e agronomia, para demonstrar a aplicação prática de programação e análise de dados no agronegócio.

## 2.3. Metodologia

O desenvolvimento do projeto foi realizado em várias etapas, envolvendo a análise do problema, criação da solução e avaliação dos resultados.

Primeiro, analisamos os requisitos do sistema para identificar as funcionalidades necessárias. Em seguida, definimos os parâmetros agronômicos, como espaçamento entre linhas e a dose de fertilizante para milho e soja.

Após essa etapa, o sistema foi construído em Python, usando listas para armazenar informações das lavouras. Implementamos funções para calcular a área, o número de ruas de plantio, a estimativa de plantas e a quantidade de fertilizante.

Além disso, utilizamos a linguagem R para conectar à API meteorológica, permitindo a coleta e exibição de dados climáticos. Os dados gerados foram exportados para um arquivo CSV, permitindo análises estatísticas na linguagem R. Por fim, realizamos análises descritivas, incluindo cálculos de média e desvio padrão, além de criar gráficos para visualizar as informações.

# <a name="c3"></a>3. Desenvolvimento do Projeto

## 3.1. Tecnologias Utilizadas

Para o desenvolvimento do projeto, foram usadas as seguintes tecnologias e ferramentas:
    
    Python – principal linguagem para criar a aplicação.
    R – usada para análise estatística dos dados.
    CSV – formato para exportar e trocar dados entre Python e R.
    GitHub – plataforma para controle de versão e colaboração.
    Terminal – usado para executar o sistema.

Essas tecnologias foram escolhidas por serem comuns em projetos de ciência de dados, inteligência artificial e análise de dados.

## 3.2. Modelagem e Algoritmos

Utilizamos uma abordagem com algoritmos determinísticos para realizar os cálculos necessários para o planejamento agrícola.Os principais algoritmos incluem:
    
    Cálculo da área do terreno com base nas dimensões fornecidas.
    Estimativa do número de ruas de plantio, considerando o espaçamento.
    Estimativa da quantidade de plantas na área cultivada.
    Cálculo da quantidade de fertilizante necessária, baseado na área em hectares.

Esses cálculos foram implementados em funções Python, promovendo a modularização do código e a organização do sistema. Os dados gerados são armazenados em listas, facilitando a manipulação e atualização das informações.Embora o projeto não utilize modelos avançados de aprendizado de máquina, ele ilustra como algoritmos podem apoiar a tomada de decisões na agricultura digital.

## 3.3. Treinamento e Teste

Como o projeto usa algoritmos determinísticos, não foi necessário um processo tradicional de treinamento de modelos de IA.

Realizamos testes funcionais para garantir que os cálculos estivessem corretos. Esses testes envolveram a inserção de diferentes valores para área, espaçamento e fertilizante, para avaliar o desempenho do sistema.

Os resultados foram analisados com estatísticas descritivas usando R, incluindo cálculos de média e desvio padrão das variáveis geradas, como a área de plantio e a quantidade de fertilizante.Esses testes ajudaram a verificar a consistência dos cálculos e a validar o funcionamento da aplicação desenvolvida.

# <a name="c4"></a>4. Resultados e Avaliações

## 4.1. Análise dos Resultados

A aplicação desenvolvida apresentou resultados consistentes para o cálculo dos principais indicadores agrícolas utilizados no planejamento de lavouras, como área de plantio, número de ruas, estimativa de plantas e quantidade de fertilizante necessária. Esses resultados foram gerados a partir de dados inseridos pelo usuário, como dimensões do terreno, espaçamento entre linhas e dose de fertilizante.

Os resultados esperados do sistema eram a obtenção de valores aproximados que pudessem representar cenários reais de planejamento agrícola. Durante os testes realizados, os cálculos retornaram valores coerentes com os parâmetros agronômicos utilizados para as culturas de milho e soja. Por exemplo, o cálculo da área do terreno e a conversão para hectares permitiram estimar corretamente a quantidade de fertilizante necessária, considerando a faixa de 300 a 400 kg por hectare.

A estimativa do número de ruas de plantio também apresentou resultados adequados, uma vez que foi baseada no espaçamento entre linhas escolhido pelo usuário dentro dos intervalos recomendados para cada cultura. Dessa forma, o sistema conseguiu representar de forma simplificada a organização da lavoura em campo.

Os dados gerados pela aplicação foram exportados para um arquivo no formato CSV e posteriormente analisados utilizando a linguagem R. A partir dessa análise, foram calculadas métricas estatísticas como média e desvio padrão das variáveis geradas pelo sistema, permitindo observar a variação dos dados entre diferentes cenários de plantio inseridos durante os testes. Além disso, foram gerados gráficos para facilitar a visualização das informações, contribuindo para uma melhor interpretação dos resultados.

Um aspecto adicional importante do projeto foi a utilização da linguagem R para integrar dados externos ao sistema. Nesse caso, foi utilizada uma API meteorológica pública para coletar informações climáticas, como temperatura e condições do tempo. O script em R realizou a conexão com a API, processou os dados retornados e exibiu as informações meteorológicas em formato de texto simples no terminal.

A inclusão desses dados climáticos demonstra como informações externas podem ser integradas a sistemas de agricultura digital, uma vez que fatores climáticos influenciam diretamente o planejamento agrícola e a tomada de decisão no campo.

De forma geral, os resultados obtidos estiveram alinhados com os resultados esperados para o funcionamento da aplicação. As pequenas diferenças observadas entre valores estimados e situações reais de campo podem ocorrer devido à simplificação dos modelos utilizados, uma vez que fatores como variabilidade do solo, condições climáticas específicas e práticas de manejo não foram considerados nos cálculos do sistema.

Mesmo assim, o projeto demonstrou de forma eficaz como ferramentas computacionais podem ser utilizadas para auxiliar no planejamento agrícola e na análise de dados, representando um exemplo prático de aplicação de tecnologias digitais no contexto da agricultura.

## 4.2. Feedback dos Usuários

*Inclua feedback recebido de usuários finais durante o processo de avaliação do projeto.*

# <a name="c5"></a>5. Conclusões e Trabalhos Futuros

*Descreva de que formas a solução desenvolvida atingiu os objetivos do projeto. Indique pontos fortes e pontos a melhorar. Relacione os pontos de melhorias evidenciados e elabore um plano de ações para serem implementadas no futuro.*

# <a name="c6"></a>6. Referências

_Incluir as principais referências de seu projeto, para que outros possam consultar caso tenham interesse em aprofundar._

# <a name="c7"></a>Anexos

*Inclua aqui quaisquer complementos para seu projeto, como diagramas, imagens, tabelas etc. Organize em sub-tópicos utilizando headings menores (use ## ou ### para isso).*
