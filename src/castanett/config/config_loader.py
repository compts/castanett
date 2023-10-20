from castanett.application.reference import DEFAULT_FRAMEWORK_CONFIGURATION
class ConfigLoader():
    def __init__(self,arg):
        self.local_var_app = {};
        self.__updatecGlobalValue(arg);

    def __execGlobalValue(self):
        self.__updatecGlobalValue()

    def __updatecGlobalValue(self,arg):
        for k,v in DEFAULT_FRAMEWORK_CONFIGURATION.items():
            if k in arg:
                self.local_var_app[k] = arg[k]
            else:
                self.local_var_app[k] = v

    def setConfig(self,arg={}):

        self.__updatecGlobalValue(arg);

    def defineConfig(self):

        return self.local_var_app;
