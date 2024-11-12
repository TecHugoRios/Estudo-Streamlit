import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="AquaSpy", layout="wide")

def AquaSpy():
    st.title("AquaSpy")

    df = pd.DataFrame(np.random.randn(15, 1), columns=(["A"]))
    my_data_element = st.line_chart(df)

    for tick in range(20):
        time.sleep(.2)
        add_df = pd.DataFrame(np.random.randn(1, 1), columns=(["A"]))
        my_data_element.add_rows(add_df)

    st.button("Regenerate")


pg = st.navigation([st.Page(AquaSpy),st.Page("Dashboard.py"),st.Page("Predição.py"),st.Page("Eventos.py"),st.Page("Denuncia.py")])

pg.run()