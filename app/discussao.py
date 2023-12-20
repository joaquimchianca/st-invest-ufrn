import streamlit as st

def app():
# Discussão dos Resultados
    st.title("Discussão dos Resultados")
    st.markdown("---")
    st.image("https://cdn-icons-png.flaticon.com/512/5064/5064943.png")
    st.markdown("""
    ## Análise e Implicações

    Neste estudo, analisamos o desempenho do Ibovespa, Bitcoin e investimentos em Renda Fixa. Observamos variações significativas nos retornos, refletindo diferentes perfis de risco e volatilidade dos ativos.

    ### Estratégia Buy and Hold
    - **Volatilidade das Criptomoedas**: A estratégia de 'buy and hold' pode não ser ideal para ativos altamente voláteis como o Bitcoin. Investidores que adotam essa estratégia devem estar preparados para as flutuações extremas que são comuns no mercado de criptomoedas.
    - **Correções no Índice da Bolsa**: O Ibovespa, embora tenha mostrado um bom retorno, está sujeito a correções de mercado. Investidores devem considerar a diversificação para mitigar riscos.

    ### Fatores Econômicos
    - **Influência do Dólar no Bitcoin**: A valorização do Bitcoin em reais também reflete as variações na cotação do dólar, o que adiciona uma camada de complexidade e risco para investidores brasileiros.
    - **Imposto sobre Renda Fixa**: O retorno da Renda Fixa deve ser considerado líquido de impostos, o que pode reduzir significativamente o ganho real para o investidor.

    ## Limitações do Estudo
    - **Período de Análise**: Limitações temporais podem afetar a generalização dos resultados. Um período de análise mais longo poderia fornecer insights adicionais, especialmente para ativos voláteis como o Bitcoin.
    - **Exclusão de Outros Fatores Externos**: Fatores como mudanças políticas e econômicas globais, que podem influenciar significativamente os mercados financeiros, não foram considerados detalhadamente.

    ## Sugestões para Pesquisas Futuras
    - **Análise de Diversificação de Portfólio**: Estudos futuros podem explorar a eficácia da diversificação de portfólio em diferentes cenários de mercado.
    - **Impacto de Fatores Macroeconômicos**: Investigar como eventos macroeconômicos globais afetam esses diferentes tipos de investimentos.
    - **Estudos Longitudinais**: Realizar análises ao longo de diferentes ciclos de mercado para entender melhor a performance de longo prazo dos ativos.
    """)


