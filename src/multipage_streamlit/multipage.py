import streamlit as st

# Reference: https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030

class MultiPage: 
    def __init__(self) -> None:
        self.pages = {}
        self._run_styles = dict(
            selectbox = self.run_selectbox,
            expander = self.run_expander,
            radio = self.run_radio
        )
        self.styles = self._run_styles.keys()
    
    def add(self, title, run) -> None: 
        self.pages[title] = run

    def run_selectbox(self, label="Navigation"):
        title = st.sidebar.selectbox(label, list(self.pages.keys()))
        self.pages[title]()

    def run_expander(self):
        for title, run in self.pages.items():
            with st.expander(title):
                run()

    def run_radio(self, label="Navigation"):
        title = st.sidebar.radio(label, list(self.pages.keys()))
        self.pages[title]()

    def run(self, style:str):
        self._run_styles[style]()