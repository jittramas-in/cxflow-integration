import os 
import sys 
import logging
if __name__ == '__main__': 
    for arg in sys.argv[1:]: 
        os.remove(arg)
        logging.warning('Watch out!111111')