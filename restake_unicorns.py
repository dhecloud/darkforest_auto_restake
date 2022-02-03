import config
from utils.darkforest_utils import exitForest, safeTransferFrom
import time
import logging

logging.basicConfig(filename='restake_unicorns.log', encoding='utf-8', level=logging.DEBUG, force=True)



def main():
    info = {
        'sender_address': config.ADDR,
        'private': config.PRIVATE_KEY,
        'intervals': config.TX_INTERVALS
    }
    #
    while 1:
        for uni in config.unicorns:
            exitForest(info, uni)
            time.sleep(config.TX_INTERVALS)
            safeTransferFrom(info, uni)
            time.sleep(config.TX_INTERVALS)

        time.sleep(config.RESTAKE_FREQ)

if __name__ == '__main__':
    main()
