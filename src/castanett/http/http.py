from castanett.http.http_validation import HttpValidation
from castanett.http.http_asset_validation import HttpAssetValidation
from castanett.management.routes_config import RoutesConfig
from castanett.application.default_method import error_404
from castanett.http.response import Response

class Http:
    def __init__(self):
        pass


    def allocate_route(self):
        list_url = {};

        list_url['url'] = {}
        list_url['error'] = {}

        for v in self.variable_routes:
            loc_http = HttpValidation(args=v,environ=self.environ)
            http_status = loc_http.is_validate_method_exist()
            if http_status['status']:
                http_val = loc_http.get_values()
                if http_status['type'] == "url":
                    self.raw_routes_map.append(http_val)
                if http_status['type'] == "error":
                    self.raw_routes_error[http_val['routes']] = http_val
        self.__execute_error_http()

    def __execute_error_http(self):
        app =RoutesConfig();
        if 404 not in self.raw_routes_error:
            app.error(404,error_404)
        for v in app.assign_routes:
            self.raw_routes_error[v['routes']] = v
    def allocate_media(self):
        http_asset = HttpAssetValidation(directory = self.raw_media_directory)
        for v in self.raw_routes.assign_routes:
            if http_asset.is_asset(args=v,environ=self.environ):
                pass
        return True,[]


    def execute_response(self):
        res = Response(self.raw_routes_map,self.raw_routes_error,self.start_response,self.environ)

        return res
