# MultiPage Streamlit

## Demo
Run the demo app: https://share.streamlit.io/crxi/multipage_streamlit/main/example/demo/app.py

## Background
Recently I needed an app that supports multiple pages. However, Streamlit does not yet have such a feature.
Not surprisingly, many innovative developers have came up with their own workarounds. Often it involves using
the selectbox as a drop-down menu to offer pages. One such implementation that I like can be found here:
https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030.
It structure each page as a separate module in a package directory, which leads to a nice modular design.

While that solution works, **the pages generated do not remember their states when we switch pages**. E.g. if I
change a slider from default value of 0 to 10 on Page A and I moved to Page B to do something, then when I
switch back to Page A, the slider is again at default 0. I thought saving the values into session_state will
help, but frustratingly it does not. The reason is addressed here: https://github.com/streamlit/streamlit/issues/3925.
By design, the values of widgets stored in session_state are removed if they no longer appear on the current page.

That same ticket implemented a solution to make the values persist. It does it by intercepting "on_change"
so that it can save the value into a persistent dictionary in session_state. I thought it was pretty clever.

## What's new here?
I combined the two solutions and got something that worked for my purpose. And so I would like to
share it with the Streamlit Community.

I added some other features:
- other than a "selectbox" style, I have an option for "expander" style of pages
- concept of namespace-prefix when saving states to avoid accidental reuse of key names


## Installation
```
python -m pip install git+https://github.com/crxi/multipage_streamlit
```

## Usage
Organize your pages as follows:
```
  app.py
  pages/
   +- page_a.py
   +- page_b.py
```

Your top level app.py:
```
import multipage_streamlit as mt
from pages import page_a, page_b

app = mt.MultiPage()
app.add("Page A", page_a.run)
app.add("Page B", page_a.run)
app.run_selectbox()
# or app.run_expander() if you prefer that 
```

In each page.py:
```
import streamlit as st
import multipage_streamlit as mt

def run():
    ms = mt.State(__name__)
    # the above line is required if you want to save states across page switches.
    # you can provide your own namespace prefix to make keys unique across pages.
    # here we use __name__ for convenience.
    st.header("Page A")
    
    x = st.slider("Value X", min_value=0, max_value=100, **ms("x", 50))
```

## Feedback
Your feedback is most welcomed. You can send via "Issues" or email to crxi.code@gmail.com.
