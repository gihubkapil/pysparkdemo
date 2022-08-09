from app.config.config import *
from app.utils.logging import *

logger=getloggingSession()

logger.info("This is info log {}".format(conf()))