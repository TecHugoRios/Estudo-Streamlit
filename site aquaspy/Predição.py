import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import pandas as pd

df = pd.read_excel("plastic-waste-generation-2000-2019.xlsx")

plasticoMundo = df.loc[df['Entity'] == 'World']
plasticoMundo = pd.DataFrame(plasticoMundo)

@st.cache_data
def convert_df(df):
    #Armazena a conversão em cache para evitar o cálculo a cada nova execução
    return df.to_csv().encode("utf-8")

st.title('Dashboard de Predição')
st.subheader('Previsão da quantidade de resíduos plásticos em rios e mares')

container = st.container(border = True)

met1, met2, met3 = container.columns(3)
met1.metric(label = "Produção de Plastico Per Capita de 2010", value = f"{plasticoMundo['Total waste'][120]:,.0f}", delta = "")
met2.metric(label = "Produção de Plastico Per Capita de 2019", value = f"{plasticoMundo['Total waste'][139]:,.0f}", delta = "")
met3.metric(label = "-------------", value = "--------", delta = "0")
st.divider()

components.iframe("https://playground.powerbi.com/sampleReportEmbed", height=800, scrolling=True)

df1 = pd.read_excel("População e Plástico.xlsx")
df1 = pd.DataFrame()

csv = convert_df(df1)

st.write("Clique no botão abaixo para realizar o download da tabela CSV referente aos gráficos acima:")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="População e Plástico.csv",
    mime="text/csv",
)

st.markdown("""
---
- Criado por: Gustavo Carmo, Hugo Rios, Jenivaldo Pereira
- Contato: AquaSpy@gmail.com

&copy 2024 AquaSpy; Todos os direitos reservados.
""", unsafe_allow_html=True)
