from app.config.config import *
from app.utils.logging import *

logger=getloggingSession()
logger.info("This is info log {}".format(get_config()))

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

