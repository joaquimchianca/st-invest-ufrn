import streamlit as st
from intro import app as page1_app
from metodologia import app as page2_app
from resultados import app as page3_app
from discussao import app as page4_app
from conclusao import app as page5_app

PAGES = {
    "Introdução": page1_app,
    "Metodologia": page2_app,
    "Resultados": page3_app,
    "Discussão": page4_app,
    "Conclusão": page5_app
}

def main():
    st.sidebar.title('Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()