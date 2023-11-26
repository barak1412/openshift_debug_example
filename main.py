import time
import logging


stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(stdout_handler)

logging.info('loading...')
print('loading...')
time.sleep(60)
logging.info('yea!')
print('yea!')
time.sleep(60)
