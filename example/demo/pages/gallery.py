import streamlit as st
from multipage_streamlit import State

def run():
    state = State(__name__)
    st.header("Gallery")

    opts = "Alpha Beta Gamma Default Epsilon".split()

    c1, c2, c3 = st.columns((2,2,2))
    with c1:
        slid = st.slider("slider", min_value=0, max_value=10, key=state("slid", 5))
        sels = st.select_slider("select_slider", opts, key=state("sels", "Default"))
        numi = st.number_input("number_input", min_value=0, max_value=10, key=state("numi", 5))
        dati = st.date_input("date_input", key=state("dati"))
        timi = st.time_input("time_input", key=state("timi"))
    with c2:
        sbox = st.selectbox("selectbox", opts, key=state("sbox", "Default"))
        mbox = st.multiselect("multiselect", opts, key=state("mbox", ["Default"]))
        texi = st.text_input("text_input", key=state("texi", "Change me!"))
        texa = st.text_area("text_area", height=150, key=state("texa", "Change\nme\ntoo!"))
    with c3:
        rado = st.radio("radio", opts, key=state("rado", "Default"))
        cbox = st.checkbox("checkbox", key=state("cbox", True))
        copi = st.color_picker("color_picker", key=state("copi", "blue"))

    state.save()