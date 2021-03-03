import os
import sys

__name__ = "phunspell"
__author__ = "David Wright"
__email__ = "dvwright@cpan.org"
__version__ = "1.0.0"

# For relative imports to work in Python 3.6
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from .phunspell import Phunspell, PhunspellError # noqa F401
