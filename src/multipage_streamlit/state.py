from streamlit import session_state as ses

# References:
# - https://github.com/streamlit/streamlit/issues/4338#issuecomment-1059519626
# - https://github.com/streamlit/streamlit/issues/3925 (previous idea)

class State:
    _KEY_ = "_state_"
    def __init__(self, namespace="_TOP_"):
        self._ns = f"{namespace}:"
        if State._KEY_ not in ses:
            ses[State._KEY_] = {}
        self._saved = ses[State._KEY_]
        self._keys = []

    def __call__(self, key, default=None):
        key = self._ns + key
        if key not in ses:
            if key in self._saved: # restore saved value
                ses[key] = self._saved[key]
            elif default is not None: # otherwise set to default if given
                ses[key] = self._saved[key] = default
        self._keys.append(key)
        return key

    def save(self):
        for key in self._keys:
            self._saved[key] = ses[key]
    
    def get(self, key, default=None):
        key = self._ns + key
        return self._saved.get(key, default)