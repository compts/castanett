from castanett.management.boot_loader_init import BootloaderInit
from castanett.config.config_loader import ConfigLoader

class Executeloader(BootloaderInit):

    def initConfig(self):
        self.config_load = ConfigLoader({})

    def defineRoutes(self,value):
        self.setRoutes(value);

    def defineConfig(self,value):
        self.config_load.setConfig(arg=value)
        self.setConfig(self.config_load.defineConfig());

    def execute_page(self,host="localhost",port=8080):
        self.execute(host=host,port=port);

    def page_call_exec(self,environ, start_response):
        return self.load_page_content(environ, start_response);
