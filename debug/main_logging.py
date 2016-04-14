import logging
import logging.config

from debug import sub_logging

logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')

logger = logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module \'sub_logging\'...')


logger.debug('let\'s test sub_logging.testLogger()')
sub_logging.testLogger()

root_logger.info('finish test...')