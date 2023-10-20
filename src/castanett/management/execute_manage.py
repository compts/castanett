from castanett.http.server import Server
class ExecuteManage:

    def __init__(self):
        self.local_routes=null;
        self.local_config=null;

    def  setRoutes(self,classs):

        self.local_routes = classs;


    def  setConfig(self,classs):
        self.local_config = classs;


    def  getRoutes(self):

        return self.local_routes;


    def getConfig(self):
        return self.local_config;
    def load_views(self,environ, start_response):

        http_class = Server()
        http_class.set_middle_ware(middle_ware=self.local_config["MIDDLEWARE"])
        http_class.set_media_directory(directory=self.local_config["MEDIA_DIRECTORY"])
        http_class.set_routes(routes=self.local_routes.assign_routes)
        http_class.set_environ(environ)
        http_class.set_start_response(start_response)
        http_class.execute()

        return http_class.execute_response().execute()
