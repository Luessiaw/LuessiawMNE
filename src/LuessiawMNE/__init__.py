__version__ = 25.0309
__author__ = "Luessiaw"

from .LuessiawSolver import *
from .exceptions import LuessiawMNEError
# print("hello")
import logging


logger = logging.getLogger("LuessiawMNE")
logger.addHandler(logging.NullHandler())

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s', 
    level=logging.INFO,
    datefmt='%H:%M:%S'
)

