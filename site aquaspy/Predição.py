import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Dashboard de Predição')
col1,col2,col3,col4 = st.columns(4)
col5,col6 = st.columns(2)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

col1.pyplot(fig)
col2.pyplot(fig)
col3.pyplot(fig)
col4.pyplot(fig)
col5.pyplot(fig)
col6.pyplot(fig)
