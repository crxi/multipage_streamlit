import streamlit as st

# Reference: https://github.com/streamlit/streamlit/issues/3925

class State():
    SAVED = "_saved_"
    def __init__(self, namespace="TOP"):
        self.ns = f"{namespace}:"
        ses = st.session_state
        if State.SAVED not in ses:
            ses[State.SAVED] = {}
        self.saved = ses[State.SAVED]
    
    def __call__(self, key, default=None, on_change=None, args=None, kwargs=None):
        key = self.ns + key
        ses = st.session_state
        if key not in ses: # restore value before creating widget
            if key in self.saved:
                ses[key] = self.saved[key]
            elif default is not None:
                ses[key] = self.saved[key] = default
        
        def _on_change():
            self.saved[key] = ses[key]
            if on_change is not None:
                on_change(*args, **kwargs)

        return {"on_change":_on_change, "key":key} #, "args":args, "kwargs":kwargs}

    def get(self, key, default=None):
        key = self.ns + key
        return self.saved.get(key, default)