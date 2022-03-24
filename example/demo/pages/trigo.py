import streamlit as st
import multipage_streamlit as mt
import numpy as np
import pandas as pd

def run():
    ms = mt.State(__name__) # use namespace to keep keys unique in session_state
    st.header("Trigonometry")

    c1,c2,c3= st.columns(3)
    with c1:
        x = st.slider("Max x", min_value=1.0, max_value=30.0, step=0.1, **ms("x", 6.0))
    with c2:
        n = st.slider("Noise", min_value=0.0, max_value=1.0, step=0.1, **ms("n", 0.0))
    with c3:
        fn = st.radio("Function", ["sine", "cosine"], **ms("fn"))
        f = np.sin if fn == "sine" else np.cos

    np.random.seed(0)
    df = pd.DataFrame(index=np.linspace(0,x,500))
    df[fn] = f(df.index) + (2*np.random.random(len(df))-1) * n
    st.line_chart(df)