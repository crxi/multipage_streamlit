import streamlit as st
from multipage_streamlit import State
import numpy as np
import pandas as pd

def run():
    state = State(__name__)
    st.header("Trigonometry")

    c1,c2,c3= st.columns(3)
    with c1:
        x = st.slider("Max x", min_value=1.0, max_value=30.0, step=0.1, key=state("x", 6.0))
    with c2:
        n = st.slider("Noise", min_value=0.0, max_value=1.0, step=0.1, key=state("n", 0.0))
    with c3:
        fn = st.radio("Function", ["sine", "cosine"], key=state("fn"))
        f = np.sin if fn == "sine" else np.cos


    np.random.seed(0)
    df = pd.DataFrame(index=np.linspace(0,x,500))
    df[fn] = f(df.index) + (2*np.random.random(len(df))-1) * n
    st.line_chart(df)

    state.save()