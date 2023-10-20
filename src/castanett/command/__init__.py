import sys 
from castanett.config.command import HEADER

def autoload():
     
    PATH = sys.argv[0]
    COMMAND = sys.argv[1:]
    TEMPLATE = "%s" % (HEADER)
    print(TEMPLATE)
