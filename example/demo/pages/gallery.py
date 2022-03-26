import streamlit as st
import multipage_streamlit as mt

def run():
    ms = mt.State(__name__)
    st.header("Gallery")

    opts = "Alpha Beta Gamma Default Epsilon".split()

    c1, c2, c3 = st.columns((2,2,2))
    with c1:
        slid = st.slider("slider", min_value=0, max_value=10, **ms("slid", 5))
        sels = st.select_slider("select_slider", opts, **ms("sels", "Default"))
        numi = st.number_input("number_input", min_value=0, max_value=10, **ms("numi", 5))
        dati = st.date_input("date_input", **ms("dati"))
        timi = st.time_input("time_input", **ms("timi"))
    with c2:
        sbox = st.selectbox("selectbox", opts, **ms("sbox", "Default"))
        mbox = st.multiselect("multiselect", opts, **ms("mbox", ["Default"]))
        texi = st.text_input("text_input", **ms("texi", "Change me!"))
        texa = st.text_area("text_area", height=150, **ms("texa", "Change\nme\ntoo!"))
    with c3:
        rado = st.radio("radio", opts, **ms("rado", "Default"))
        cbox = st.checkbox("checkbox", **ms("cbox", True))
        copi = st.color_picker("color_picker", **ms("copi", "blue"))