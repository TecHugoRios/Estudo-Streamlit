import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from streamlit_option_menu import option_menu

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

plasticoMundo = pd.read_excel("plastic-waste-generation-2000-2019.xlsx")
plasticoMundo = pd.DataFrame(plasticoMundo)

st.set_page_config(page_title="AquaSpy", layout="wide")

def AquaSpy():
    st.title("AquaSpy")
    st.subheader("Transparência das águas para todos.")
    st.divider()

    st.write("A proposta central do AquaSpy é fornecer acesso direto e em tempo real aos dados propostos e interatividade ao usuário. Isso será feito por meio da disponibilização de uma página com eventos relacionados ao assunto que vão ocorrer e a predição relacionado ao futuro desses dados, assim permitindo que os usuários tomem decisões informadas e participem ativamente das políticas de sustentabilidade. Por meio deste portal, busca-se construir uma interface que seja intuitiva, acessível e relevante, de forma a representar de maneira clara como o produto será desenvolvido e quais benefícios trará para o meio ambiente.")
    
    st.write("Segue abaixo um gráfico mostrando a quantidade de resíduos plasticos em rios e mares pelo mundo, de 2000 até 2019: ")
    
    plt.style.use('_mpl-gallery')
    df = pd.read_excel("plastic-waste-generation-2000-2019.xlsx")

    plasticoMundo = df.loc[df['Entity'] == 'World']

    x = plasticoMundo["Year"]
    y = plasticoMundo["Total waste"]

    # Criar gráfico usando Matplotlib
    plt.figure(figsize=(10,6))
    plt.plot(x,y, color='blue', linestyle="--")
    plt.xticks(ticks=plasticoMundo['Year'], labels=plasticoMundo['Year'].astype(int))
    plt.scatter(x,y, color='red')
    plt.title("Total de Plástico no Mundo")
    plt.xlabel("Anos")
    plt.ylabel("Desperdício Total (toneladas)")
    plt.legend(['Estimativa', 'Dado'])
    plt.tight_layout()
    
    # Exibir o gráfico no Streamlit
    st.pyplot(plt)

    csv = convert_df(plasticoMundo)
    st.write("Clique no botão abaixo para realizar o download da tabela CSV referente ao gráfico acima:")
    st.download_button(
        label="Download",
        data=csv,
        file_name="População e Plástico.csv",
        mime="text/csv",
    )

    st.markdown("""
    ---
    - Criado por: Gustavo Carmo, Hugo Rios, Jenivaldo Pereira
    - Contato: AquaSpy@gmail.com

    © 2024 AquaSpy\n
    Todos os direitos reservados.
    """, unsafe_allow_html=True)

    
pg = st.navigation([st.Page(AquaSpy),st.Page("Dashboard.py"),st.Page("Predição.py"),st.Page("Eventos.py"),st.Page("Denuncia.py")])

pg.run()