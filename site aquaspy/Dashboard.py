import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

@st.cache_data
def convert_df(df):
    #Armazena a conversão em cache para evitar o cálculo a cada nova execução
    return df.to_csv().encode("utf-8")

df = pd.read_excel("plastic-waste-generation-2000-2019.xlsx")

plasticoMundo = df.loc[df['Entity'] == 'World']
plasticoMundo = pd.DataFrame(plasticoMundo)

df2 = pd.read_excel("População e Plástico.xlsx")
df2 = pd.DataFrame(df2)

populacao = df2.loc[df2['Population - Sex: all - Age: all - Variant: estimates'] == 'World']

st.title('Dashboard')
container = st.container(border = True)

met1, met2, met3 = container.columns(3)
met1.metric(label = "Plastico Per Capita de 2000", value = f"{plasticoMundo['Total waste'][120]:,.0f}", delta = "")
met2.metric(label = "Plastico Per Capita de 2019", value = f"{plasticoMundo['Total waste'][139]:,.0f}", delta = "")
met3.metric(label = "---------", value = f"----------", delta = "0")
st.divider()

components.iframe("https://playground.powerbi.com/sampleReportEmbed", height=800, scrolling=True)

csv = convert_df(df2)

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
