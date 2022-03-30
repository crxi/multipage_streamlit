import streamlit as st
from multipage_streamlit import State
import numpy as np
import pandas as pd

def run():
    state = State(__name__) # use namespace to keep keys unique in session_state
    st.header("Histogram")
    
    c1, c2 = st.columns(2)
    with c1:
        x = st.slider("Sample Size", min_value=100, max_value=1000, key=state("x", 300))
    with c2:
        n = st.slider("Bin Size", min_value=5, max_value=50, key=state("n", 25))

    np.random.seed(1)
    sample = np.random.normal(50, 8, x)
    histo = np.histogram(sample, bins=n, range=(0,100))
    st.bar_chart(histo[0])

    state.save()