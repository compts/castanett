from castanett.http.wsgi import WSGI
from castanett.management.execute_manage import ExecuteManage

class BootloaderInit(ExecuteManage):

    def execute(self,host="localhost",port=8080):

        app_wsgi = WSGI()
        app_wsgi.address(host=host,port=port)
        view = self.load_views
        app_wsgi.activate_server(view)

    def load_page_content(self,environ, start_response):
        view = self.load_views(environ,start_response)

        return view['content']

