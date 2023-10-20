from castanett.initialize.execute_loader import Executeloader
from urllib.parse import urlparse, quote
import os

class Castanett(Executeloader):
    def __init__(self,name="Castanett"):
        self.local_name = name;
        self.cwd = os.getcwd()
        self.initConfig()
        self.config_load.setConfig(arg={"MEDIA_DIRECTORY":[self.cwd]})

    def setDefaultConfig(self,value):
        self.defineConfig(value);
    def setDefaultRoute(self,value):
        self.defineRoutes(value);
    def run(self,host="localhost",port=8080):
        self.execute_page(host=host,port=port);

    def __call__ (self,environ, start_response):
        html = self.page_call_exec(environ, start_response)

        html_test = """
                <html>
                     Hello world
                </html>
                """


        response_body = html


        status = '200 OK'

        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))
        ]

        start_response(status, response_headers)
        return [response_body]

    def __repr__(self):
        return '<%s %r>' % (
            self.__class__.__name__,
            self.name,
        )
