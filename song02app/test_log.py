import logging


logging.basicConfig(format='%(levelname)s:%(message)s', filename='testlog.log', level=logging.DEBUG,  datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')