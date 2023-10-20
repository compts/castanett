from castanett.core.support import *
import re

class HttpAssetValidation:
    def __init__(self,directory=[]):
        self.directory = directory

    def is_asset(self,args={},environ={}):
        self.args = args
        self.values = {}
        self.bool_validate = False
        self.environ = environ

        if re.search(r'\.[a-z]{2,}',self.environ['PATH_INFO']):
            pass
        else:
            return False
