# MultiPage Streamlit
MultiPage Streamlit app with persistent widget states

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
so that it can save the value into a persistent dictionary in session_state. I thought it was pretty clever,
although it does add some complexity if we want to use "on_change".

Then I came across this: https://github.com/streamlit/streamlit/issues/4338. The purposed solution (in the comment)
had a different approach which does not involve using "on_change". While it did not work out-of-the-box for me as my
app spanned different modules, it inspired me to come up with a different solution.

## What's new here?
I combined the solutions and got something that worked for my purpose. And so I would like to
share it with the Streamlit Community.

I added some other features:
- 3 different styles of multipage app: selectbox, expander and radio.
- allow setting of default value when declaring key name
- concept of namespace-prefix when saving states to avoid accidental reuse of key names (especially if the
  pages span multiple modules)


## Installation
From PyPI:
```bash
python -m pip install multipage_streamlit
```
From GitHub:
```bash
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
```python
import multipage_streamlit as mt
from pages import page_a, page_b

app = mt.MultiPage()
app.add("Page A", page_a.run)
app.add("Page B", page_a.run)
app.run_selectbox()
# alternatives: app.run_expander() or app.run_radio() if you prefer those 
```

In each page.py:
```python
import streamlit as st
from multipage_streamlit import State

def run():
    state = State(__name__)
    # the above line is required if you want to save states across page switches.
    # you can provide your own namespace prefix to make keys unique across pages.
    # here we use __name__ for convenience.
    st.header("Page A")
    
    x = st.slider("Value X", min_value=0, max_value=100, key=state("x", 50))
    # here's the "magic": state(name, default, ...) returns the namespace-prefixed
    # key name. if a previously saved state exist, the widget is set to it. if not,
    # the widget is set to default if it is specified.
    
    state.save()  # MUST CALL THE ABOVE TO SAVE THE STATE!
```

See the demo for more examples.

## Feedback
Your feedback is most welcomed. You can send via "Issues" or email to crxi.code@gmail.com.

## Contributing
Interested in contributing? Check out the contributing guidelines.
Please note that this project is released with a Code of Conduct.
By contributing to this project, you agree to abide by its terms.

## License
`multipage_streamlit` was created by CRXi <crxi.code@gmail.com>.
It is licensed under the terms of the Apache License 2.0 license.

## Credits
`multipage_streamlit` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
