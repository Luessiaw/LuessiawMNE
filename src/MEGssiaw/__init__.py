__version__ = 26.0508
__author__ = "Luessiaw"

from .LuessiawSolver import *
# print("hello")
import logging


logger = logging.getLogger("LuessiawMNE")
logger.addHandler(logging.NullHandler())

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s', 
    level=logging.INFO,
    datefmt='%H:%M:%S'
)

