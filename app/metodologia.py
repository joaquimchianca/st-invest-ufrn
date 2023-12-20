import streamlit as st

def app():
    st.title("Metodologia")
    st.markdown("---")

    st.markdown("""
    **Neste estudo**, utilizamos a biblioteca `yfinance` do Python para obter os dados do índice **Ibovespa** e do **Bitcoin**. 
    Utilizamos também as bibliotecas `pandas` para *limpeza e manipulação dos dados* e `matplotlib.pyplot` para *plotar os gráficos* dos respectivos rendimentos.
    Para o *rendimento fixo*, consideramos um rendimento de **12.5% ao ano**, fazendo uma simulação num simulador de investimentos online.
    """)

    st.image("assets/met1.png")

    st.header("O que é Ibovespa?")
    st.markdown("""
    O **Ibovespa** é o principal indicador de desempenho das ações negociadas na B3, a bolsa de valores do Brasil. 
    Ele reúne as ações mais negociadas e de maior capitalização no mercado brasileiro, servindo como um termômetro para o comportamento do mercado acionário no país.
    """)
    st.image("https://bmcnews.com.br/wp-content/uploads/2023/12/AAREVXYER5DRRKT7GRSINHBHJM-1024x536.jpg")

    st.header("O que é Bitcoin?")
    st.markdown("""
    **Bitcoin** é uma criptomoeda digital, usada para transações e investimentos online. 
    Ela é *descentralizada* e opera sem a necessidade de um banco central ou administrador único. 
    O Bitcoin é a primeira e mais conhecida criptomoeda, muitas vezes considerada como o padrão ouro das moedas digitais.
    """)
    st.image("https://cointimes.com.br/wp-content/uploads/2018/07/O-que-e-Bitcoin.jpeg")

    st.header("O que é Renda Fixa?")
    st.markdown("""
    **Renda fixa** é uma categoria de investimento onde os retornos são, em teoria, previsíveis. 
    Inclui ativos como *títulos públicos, CDBs, LCIs, LCAs*, entre outros. 
    Investidores em renda fixa emprestam dinheiro em troca de um retorno fixo ou variável, mas previsível, baseado em juros.
    """)

    st.header("Análise de Dados")
    st.markdown("""
    Nesta análise, consideramos um **investimento inicial de R$ 1.000,00**. Observamos o comportamento desse valor ao longo de 72 meses, seguindo os rendimentos (variável ou fixo) de cada ativo.

    Para o **Bitcoin**, convertemos o valor para dólar com a cotação da data inicial (01/11/2017). Dessa forma, criamos gráficos observando tanto o **valor em dinheiro**, quanto a **variação em porcentagem** com base no investimento inicial neste intervalo de tempo.

    O download de dados nos fornece os valores de abertura e fechamento de cada dia, logo foi calculado a diferença entre esse valores, o que nos dá o rendimento.
    Em cima dos valores de rendimento, podemos observar o como o valor investido se comporta.
    
    Para uma análise mais generalista, como temos os valores diários, os gráficos só mostram os valores para o último dia de cada mês. 
    """)

    # Aqui você pode adicionar o código para exibir os gráficos e outras análises.
    
