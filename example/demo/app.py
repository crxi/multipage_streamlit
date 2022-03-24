import streamlit as st
st.set_page_config(layout="wide")

st.title("MultiPage Streamlit Demo")
st.text("""
  Change some settings. Then switch between Histogram and Trigonometry.
  Observe that the settings are persisted even as we switch pages.
  """)

# This is how we create a multipage app
import multipage_streamlit as mt
from pages import histo, trigo
app = mt.MultiPage()
app.add("Histogram", histo.run)
app.add("Trigonometry", trigo.run)

# We show 2 different styles of multipage apps; typically we just use one
style = st.sidebar.radio("MultiPage style:", ["selectbox", "expander"],
                          help="Choose the style of the multipage app")
if style == "selectbox":
   app.run_selectbox()
else:
   app.run_expander()

# Show session_state to the curious
if st.sidebar.checkbox("Show session_state", help="See namespaces and saved states"):
   st.sidebar.write(st.session_state)