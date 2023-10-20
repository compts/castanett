from castanett.application.reference import HTTP_STATUS_CODES,DEFAULT_RESPONSE_HEADER
from castanett.http.request import Request

class Response():
    def __init__(self,uri,uri_error,start_response,environ):

        self.uri = uri
        self.uri_error = uri_error
        self.start_response = start_response
        self.environ = environ
    def execute(self):
        error_code = 404
        PATH_INFO = self.environ['PATH_INFO'].strip("/")
        REQUEST_METHOD = self.environ['REQUEST_METHOD']

        for value in self.uri:
            routes = value['routes'].strip("/")
            action = value['action']
            option = value['option']

            option_method = value['option']['method']
            option_parameter = value['option']['parameter']


            if PATH_INFO == routes:
                request = Request({},self.environ)
                action_str = action(request)
                if action_str.status == 200:
                    return {
                        'content':action_str.content,
                        'status':200,
                        'header':[]
                    }
                else:
                    error_code  = action_str.status

        if error_code in self.uri_error:
            return {
                'content': self.uri_error[error_code]['action'](),
                'status': error_code,
                'header':[]
            }
        return {
                'content':"Server unavailable",
                'status':500,
                'header':[]
            }
