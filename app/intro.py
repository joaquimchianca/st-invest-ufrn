import streamlit as st

def app():
    st.title("Análise de estratégia Buy and Hold")
    st.title("Bitcoin VS Ibovespa Vs Rendimento Fixo")
    st.write("Pesquisa feita por Joaquim Chianca.")
    st.markdown("---")

    st.image("https://moneylion.nyc3.cdn.digitaloceanspaces.com/wp-content/uploads/2023/01/06170512/Untitled-design-88.webp")

    st.subheader("Qual foi o melhor rendimento em 72 meses?")

    st.subheader("Neste estudo, observamos o rendimento das três opções de investimento. Partindo de um valor inicial de R$ 1000,00.")
    st.subheader("O objetivo é saber qual foi a melhor opção no fim do intervalo de tempo entre 01/11/2017 até 30/10/2023.")
    st.subheader("Além disso, comentar sobre a escolha da estratégia Buy and Hold.")

    texto = """
    Investir é essencial para a saúde financeira e crescimento de capital. Em um mundo de incertezas econômicas, investimentos sábios garantem segurança financeira e realização de metas pessoais e profissionais. O investimento é crucial para o crescimento de capital, permitindo alcançar objetivos de longo prazo, como aposentadoria, aquisição de imóveis ou educação dos filhos.

    Além disso, investir combate a inflação, que erode o poder de compra do dinheiro. Investimentos com retornos acima da inflação preservam ou aumentam o valor real do capital. Sem investir, o dinheiro economizado perde valor, afetando a capacidade futura de compra.

    Investimentos também geram renda passiva, como dividendos de ações e rendimentos de aluguéis, complementando outras fontes de receita ou sustentando indivíduos em diferentes fases da vida.
    """

    st.write(texto)

    