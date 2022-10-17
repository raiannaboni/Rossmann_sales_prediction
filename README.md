# Rossmann Drugstore Sales Prediction

![shop_rossmann-690x460](https://user-images.githubusercontent.com/102910250/196037511-40138caf-fa87-45e6-81d6-7b875765bd7f.jpg)

Este repositório contém códigos para a predição de vendas da rede de farmácias Rossmann, localizada na Europa, possuindo mais de 4000 lojas em sete diferentes países.

Os dados utilizados neste projeto são reais e foram disponibilizados pela Rossmann no [Kaggle](https://www.kaggle.com/c/rossmann-store-sales). Apesar de o problema de negócio ser fictício, ele corresponde a um problema real: prever as vendas futuras das lojas para o planejamento das finanças da empresa.

## 1. O problema de negócio

O CFO da empresa convocou uma reunião com o time de dados e informou que as lojas precisavam passar por reformas. Portanto, ele gostaria de saber qual seria o faturamento das lojas nas próximas 6 semanas para que as reformas fossem programadas de acordo com o faturamento da empresa.

Foi pedido à cientista de dados, então, que desenvolvesse um modelo de previsão de vendas que determinasse o faturamento de cada loja nas próximas 6 semanas.

## 2. Resultado do modelo

O modelo previu que nas próximas 6 semanas o faturamento de todas as lojas seria de $286.435.616,00, com um erro médio absoluto (MAE) de 765 para cada loja - no melhor cenário, a empresa fatura $287.291.675,81 e no pior cenário, R$285.579.535,63.

## 3. Premissas do negócio

- O dataset possui 1115 lojas e as vendas estão dentro do período de 01/01/2013 a 31/07/2015.
- Os dias nos quais as lojas estão fechadas foram retirados da análise.
- Para as lojas com valor nulo na coluna de competidor próximo (competition_distance), foi considerado que não havia competidores por perto. Para futura utilização desse dado na fase de "feature engineering", o valor nulo foi trocado por 200.000 m (duas vezes o maior valor disponível). 

As variáveis do dataset original são as seguintes:

| Variável |	Definição |
| --- | --- |
| store |	id único de cada loja
| day_of_week |	indica o dia da semana que era aquele dia (começando com 1 = domingo)
| date |	data da venda
| sales |	faturamento da loja naquele dia
| customers |	número de clientes na loja naquele dia
| open |	loja aberta ou fechada (0 = closed, 1 = open)
| state_holiday |	feriado nacional (a = public holiday, b = Easter holiday, c = Christmas, 0 = Dia Comum)
| school_holiday |	indica se a loja naquele dia foi afetada pelo fechamento das escolas públicas
| store_type |	modelo da loja (a, b, c ou d)
| assortment |	nível de sortimento da loja (a = basic, b = extra, c = extended)
| competition_distance |	distancia, em metros, do competidor mais próximo
| competition_open_since_month |	mês da abertura do competidor mais próximo
| competition_open_since_year |	ano da abertura do competidor mais próximo
| promo |	se a loja está ou não com uma promoção ativa naquele dia
| promo2 |	indica se é uma promoção contínua e consecutiva (0 = store not participating, 1 = store participating)
| promo2_since_week |	semana do calendário na qual a loja entrou em Promo2
| promo2_since_year |	ano no qual a loja entrou em Promo2
| promo_interval |	meses do ano nos quais Promo2 é iniciada (ex: "Feb,May,Aug,Nov")

As variáveis criadas na fase de "feature engineering" foram as seguintes:

| Variável | Definição |
| --- | --- |
| year | ano no qual a venda foi realizada |
| month | mês no qual a venda foi realizada |
| day | dia no qual a venda foi realizada |
| week_of_year | semana do ano na qual a venda foi realizada (int type) |
| year_week | semana do ano na qual a venda foi realizada (obj type, %Y-%W) |
| competition_since | data de abertura das lojas competidoras próximas (junção de competition_open_since_month e competition_open_since_year) |
| competition_time_month | número de meses desde a abertura da loja competidora |
| promo_since | data de início da promoção (junção de promo2_since_week e promo2_since_year) |
| promo_time_week | número de semanas nas quais a promo2 estava ativa |

## 4. Estratégia de solução

O projeto foi desenvolvido seguindo o método CRISP-DS (Cross-Industry Standard Process - Data Science).

``` mermaid
journey
  title Sequência de passos
  section CRISP-DS
    
    Data Description: 5: Me
    Feature Engineering: 5: Me
    Data Filtering: 5: Me
    Exploratory Data Analysis: 5: Me
    Data Preparation: 5: Me
    Feature Selection: 5: Me
    Machine Learning Modeling: 5: Me
    Hyper Parameter Fine Tuning: 5: Me
    Model-to-Business Interpretation: 5: Me
    Model Deploy: 5: Me

```

## 5. Os 3 principais insights extraídos dos dados

**1. Lojas com competidores mais próximos vendem menos**

**Falso** - Lojas com competidores mais próximos vendem mais.

![competition_distance](https://user-images.githubusercontent.com/102910250/196230219-c069d401-8bd6-45ec-a036-bd24f455e96f.png)


**2. Lojas vendem mais no segundo semestre do ano**

**Falso** - Lojas vendem menos no segundo semestre do ano.

![semestre](https://user-images.githubusercontent.com/102910250/196231192-b4d79d76-e6b6-4424-9499-0688cec3108f.png)


**3. Lojas vendem mais depois do dia 10 de cada mês**

**Verdadeiro** - Lojas vendem mais depois do dia 10 de cada mês 

![after_before](https://user-images.githubusercontent.com/102910250/196231601-2142bea1-7ccb-4ac4-b858-7d6ebf42f889.png)


## 6. Modelo de Machine Learning

Foram testados os seguintes modelos de ML: 

- Regressão linear
- Regressão linear regularizada (Lasso)
- Random Forest regressor
- XGBoost regressor

Esses foram os resultados após o Cross-Validation (MAE = mean absolute error; MAPE = mean absolut percentage error; RSME = root mean squared error):

![Captura de tela de 2022-10-17 13-31-26](https://user-images.githubusercontent.com/102910250/196232607-a66762b2-237a-4f17-9ebd-40ee10677741.png)


O modelo selecionado foi o XGBoost e os resultados após o hypertuning são os seguintes:

![Captura de tela de 2022-10-17 13-33-32](https://user-images.githubusercontent.com/102910250/196232998-31d7d916-44a4-4390-99c2-1f43d9ccc745.png)

Performance total:

![Captura de tela de 2022-10-17 13-35-27](https://user-images.githubusercontent.com/102910250/196233630-ba3ebd9b-ec60-44ba-a8b7-0924dcb81304.png)


## 7. Bot do Telegram

As predições de vendas de cada loja para as próximas 6 semanas são entregues via bot do [Telegram](http://t.me/rossmann_raianna_bot) (Clique em Telegram para acessar o bot).

![WhatsApp Image 2022-10-17 at 13 38 34](https://user-images.githubusercontent.com/102910250/196234433-75d7f96c-78f7-4eb3-afe4-b1aa202c5fa8.jpeg)

## 8. Conclusão

O objetivo do presente projeto foi desenvolver um modelo de predição de vendas para as lojas Rossmann, e o projeto foi entregue ao CFO da empresa na forma de um bot do Telegram, onde podemos acessar o faturamento de cada empresa individualmente de forma rápida e eficaz.

## 9. Próximos passos

Seguindo o métido CRISP-DS, melhorias podem ser realizadas no modelo.

- Criar novas variáveis que podem melhorar a performance do modelo.
- Testar outros modelos de Machine Learning com melhor performance.
- Melhorar a reposta do bot do Telegram.

## 10. Referências

- Este projeto faz parte do módulo Data Science em Produção, da [Comunidade DS](https://comunidadeds.com/).
- Os dados foram coletados no [Kaggle](https://www.kaggle.com/c/rossmann-store-sales/data).






