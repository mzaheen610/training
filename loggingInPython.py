import logging

#Basic configurations
#use logging.basicConfig(filename='app.log', filemode='w', format='')

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='newlog.log', filemode='w', format='%(name)s:%(levelname)s:%(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is not a sample message")
logger.warning("OH damn")
logger.error("Systems are failing")
logger.critical("MAYDAY..... MAYDAY")
