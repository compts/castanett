class RoutesConfig:


    def __init__(self):

       self.assign_routes=[];


    def match(self,routes="",action=None,option={}):
        self.__verify_route("match",routes,action,option);


    def url(self,routes="",action=None,option={}):

        self.__verify_route("url",routes,action,option);


    def error(self,routes="",action=None,option={}):

        self.__verify_route("error",routes,action,option)

    def __options_validation(self,option={}):
        local_option = {}
        local_option["method"] = ["POST","GET"];
        local_option["parameter"] = [];

        if 'method' in option:
            local_option["method"] = option['method']

        if 'parameter' in option:
            local_option["parameter"] = isinstance(option['parameter'], dict) and option['parameter'] or {}

        return  local_option

    def __verify_route(self,method,routes="",action=None,option={}):

        local_option = self.__options_validation(option);

        self.assign_routes.append({
            "method":method,
            "routes":routes,
            "action":action,
            "option":local_option
           });

