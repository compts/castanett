from castanett.http.http import Http

class Server(Http):

    def __init__(self):
        self.variable_routes = [];
        self.raw_routes_map = [];
        self.raw_routes_error = {};
        self.environ = [];
        self.start_response = None
        self.middle_ware = [];
        self.raw_media_directory = [];


        self.is_url_request = False;
    def set_routes(self,routes=[]):
        self.variable_routes = routes

    def set_middle_ware(self,middle_ware=[]):
        self.raw_middle_ware = middle_ware

    def set_media_directory(self,directory=[]):
        self.raw_media_directory = directory

    def set_environ(self,environ):
        self.environ = environ;

    def set_start_response(self,start_response):
        self.start_response = start_response;

    def __execute_url_request(self):
        if len(self.variable_routes)>0:
            self.allocate_route()


    def __execute_media_request(self):
        if self.is_url_request == False:

            if len(self.raw_middle_ware)>0:
                path_url=self.allocate_media()

    def execute(self):
        self.__execute_url_request()
        self.__execute_media_request()
