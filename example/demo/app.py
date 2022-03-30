import streamlit as st
st.set_page_config(layout="wide")

st.title("MultiPage Streamlit Demo")
st.write("""
  Switch between the pages and change their settings.  
  Observe that the settings persisted even as we switched pages.  
  Get the code at <https://github.com/crxi/multipage_streamlit>.
""")

# This is how we create a multipage app
import multipage_streamlit as mt
from pages import histo, trigo, gallery
app = mt.MultiPage()
app.add("Histogram", histo.run)
app.add("Trigonometry", trigo.run)
app.add("Gallery", gallery.run)

# We show 3 different styles of multipage apps; typically we just use one and do
#   app.run_selectbox()
# For the sake of the demo, we allow switching between all 3 styles.
style = st.sidebar.radio("MultiPage style:", app.styles,
                              help="Choose the style of the multipage app")
app.run(style)


# Show session_state to the curious
if st.sidebar.checkbox("Show session_state", help="See namespaces and saved states"):
   st.sidebar.write(st.session_state)