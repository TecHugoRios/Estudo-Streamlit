import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")

df = pd.read_excel("plastic-waste-generation-2000-2019.xlsx")

plasticoMundo = df.loc[df['Entity'] == 'World']
plasticoMundo = pd.DataFrame(plasticoMundo)

df2 = pd.read_excel("População e Plástico.xlsx")
df2 = pd.DataFrame(df2)

populacao = df2.loc[df2['Population - Sex: all - Age: all - Variant: estimates'] == 'World']

st.title('Dashboard')
container = st.container(border = True)

met1, met2 = container.columns(2)
met1.metric(label = "Plastico Mundial Per Capita (2000)", value = f"{plasticoMundo['Total waste'][120]:,.0f}", delta = "")
difAnos = plasticoMundo['Total waste'][139] - plasticoMundo['Total waste'][120]
met2.metric(label = "Plastico Mundial Per Capita (2019)", value = f"{plasticoMundo['Total waste'][139]:,.0f}", delta = f"{difAnos:,.0f}")
#met3.metric(label = "---------", value = f"----------", delta = "0")
#st.divider()

components.iframe("https://app.powerbi.com/reportEmbed?reportId=a065dbdd-d3c2-4939-a021-fafd27af3ed3&autoAuth=true&ctid=1d90b5e6-9b17-47a4-a2fe-1884712d8c2f", height=800, scrolling=True)

csv = convert_df(df2)

st.write("Clique no botão para realizar o download dos dados acima em formato .CSV:")
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
 
© 2024 AquaSpy \n
Todos os direitos reservados.
""", unsafe_allow_html=True)
