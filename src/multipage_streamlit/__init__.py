# read version from installed package
from importlib.metadata import version
__version__ = version("multipage_streamlit")

from .multipage import MultiPage
from .state import State
