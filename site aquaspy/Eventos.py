import streamlit.components.v1 as components
import streamlit as st

st.title("Eventos")
st.subheader("Navegue pelo feed e encontre eventos relacionados à limpeza de regiões costeiras, rios ou lagos.")
st.divider()

components.iframe("https://widgets.sociablekit.com/rss-feed/iframe/25483531", height=800, scrolling=True)

st.markdown("""
---
- Criado por: Gustavo Carmo, Hugo Rios, Jenivaldo Pereira
- Contato: AquaSpy@gmail.com

© 2024 AquaSpy \n
Todos os direitos reservados.
""", unsafe_allow_html=True)