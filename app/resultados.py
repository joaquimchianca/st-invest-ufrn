import streamlit as st

def app():
    import streamlit as st

def app():
    st.title("Análise de Rendimentos: Ibovespa, Bitcoin e Renda Fixa")
    st.markdown("---")
    
    st.markdown("""
    ## Análise Comparativa de Rendimentos
    Esta seção apresenta a análise comparativa dos rendimentos do Ibovespa, Bitcoin, e Renda Fixa. 
    São exibidos dois gráficos para cada tipo de rendimento: um mostrando o valor em dinheiro ao longo do tempo e outro a variação percentual com base no investimento inicial.
    """)

    
    st.markdown("### Ibovespa")
    st.markdown("Aqui estão os gráficos referentes ao rendimento do Ibovespa:")
    st.image("graficos/ibovespa1.png", "Gráfico mostrando valor em reais.")
    st.image("graficos/ibovespa2.png", "Gráfico mostrando variação percentual.")
    st.markdown("**Nesse tipo de investimento obtivemos um retorno de R$ 1483,83. Um rendimento de 48,36% em cima do aporte inicial.**")


    # Bitcoin
    st.markdown("### Bitcoin")
    st.markdown("Aqui estão os gráficos referentes ao rendimento do Bitcoin:")
    st.image("graficos/bitcoin1.png", "Gráfico mostrando valor em reais.")
    st.image("graficos/bitcoin2.png", "Gráfico mostrando variação percentual.")
    st.markdown("**Nesse tipo de investimento obtivemos um retorno de R$ 6628,38 - considerando a cotação do dólar do último dia considerado na pesquisa. Um rendimento de 662,84%**")

    # Renda Fixa
    st.markdown("### Renda Fixa")
    st.markdown("Aqui estão os gráficos referentes ao rendimento de Renda Fixa:")
    st.image("graficos/fixo1.png", "Gráfico mostrando valor em reais.")
    st.image("graficos/fixo2.png", "Gráfico mostrando variação percentual.")
    st.markdown("**Nesse tipo de investimento obtivemos um retorno de R$ 2027,29 - isso tomando apenas o rendimento bruto, visto que é descontado um valor de imposto. Um rendimento de 102,73%**")

    # Interpretação dos Resultados
    st.markdown("## Interpretação dos Resultados")
    st.markdown("""
    Nesta seção, vamos discutir as implicações dos gráficos e o que eles representam em termos de performance de investimento. 
    A comparação entre os diferentes tipos de investimento nos oferece insights sobre a volatilidade do mercado, o retorno potencial e o perfil de risco de cada opção de investimento.
    """)

    # Ibovespa
    st.subheader("Ibovespa")
    st.markdown("""
    - **Retorno**: R$ 1483,83 (48,36% de rendimento).
    - **Comentários**: O Ibovespa, sendo o principal indicador da bolsa de valores brasileira, mostrou um desempenho robusto. Este tipo de investimento é mais indicado para investidores com perfil moderado, que buscam um equilíbrio entre risco e retorno. O rendimento de quase 50% é atraente, mas está sujeito às flutuações do mercado e eventos econômicos.
    """)

    # Bitcoin
    st.subheader("Bitcoin")
    st.markdown("""
    - **Retorno**: R$ 6628,38 (662,84% de rendimento).
    - **Comentários**: O Bitcoin, conhecido por sua alta volatilidade, proporcionou um retorno significativo. Este tipo de investimento é ideal para investidores com perfil agressivo, dispostos a assumir riscos mais altos para possíveis retornos elevados. A criptomoeda pode ser afetada por diversos fatores globais, incluindo mudanças regulatórias e tendências de mercado.
    """)

    # Renda Fixa
    st.subheader("Renda Fixa")
    st.markdown("""
    - **Retorno**: R$ 2027,29 (102,73% de rendimento).
    - **Comentários**: A renda fixa ofereceu um retorno estável e é mais adequada para investidores conservadores, que priorizam a segurança e a previsibilidade dos retornos. Apesar de um retorno superior a 100%, é importante lembrar que os rendimentos são brutos e sujeitos a impostos, o que pode reduzir o ganho líquido.
    """)