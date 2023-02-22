from src.utils import *

try:
    from alive_progress import alive_bar
except ModuleNotFoundError as error:
    print(Colors.FAIL + "the required module \"" + error.msg.split("'")[1] + "\" is missing" + Colors.ENDC)
    exit(1)

from .core import *
