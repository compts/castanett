HTTP_STATUS_CODES = {
    100:    'Continue',
    101:    'Switching Protocols',
    102:    'Processing',
    200:    'OK',
    201:    'Created',
    202:    'Accepted',
    203:    'Non Authoritative Information',
    204:    'No Content',
    205:    'Reset Content',
    206:    'Partial Content',
    207:    'Multi Status',
    226:    'IM Used',              # see RFC 3229
    300:    'Multiple Choices',
    301:    'Moved Permanently',
    302:    'Found',
    303:    'See Other',
    304:    'Not Modified',
    305:    'Use Proxy',
    307:    'Temporary Redirect',
    400:    'Bad Request',
    401:    'Unauthorized',
    402:    'Payment Required',     # unused
    403:    'Forbidden',
    404:    'Not Found',
    405:    'Method Not Allowed',
    406:    'Not Acceptable',
    407:    'Proxy Authentication Required',
    408:    'Request Timeout',
    409:    'Conflict',
    410:    'Gone',
    411:    'Length Required',
    412:    'Precondition Failed',
    413:    'Request Entity Too Large',
    414:    'Request URI Too Long',
    415:    'Unsupported Media Type',
    416:    'Requested Range Not Satisfiable',
    417:    'Expectation Failed',
    418:    'I\'m a teapot',  # see RFC 2324
    421:    'Misdirected Request',  # see RFC 7540
    422:    'Unprocessable Entity',
    423:    'Locked',
    424:    'Failed Dependency',
    426:    'Upgrade Required',
    428:    'Precondition Required',  # see RFC 6585
    429:    'Too Many Requests',
    431:    'Request Header Fields Too Large',
    449:    'Retry With',  # proprietary MS extension
    451:    'Unavailable For Legal Reasons',
    500:    'Internal Server Error',
    501:    'Not Implemented',
    502:    'Bad Gateway',
    503:    'Service Unavailable',
    504:    'Gateway Timeout',
    505:    'HTTP Version Not Supported',
    507:    'Insufficient Storage',
    510:    'Not Extended'
}
DEFAULT_FRAMEWORK_CONFIGURATION={
 'MEDIA_DIRECTORY':[],
 'MIDDLEWARE':[],
 #'APP':[],
 'DATABASE' :[],
 'SESSION' :[],
}

DEFAULT_RESPONSE_HEADER={
    'Content-Type': 'text/html'
}

REQUEST_METHOD=[
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "HEAD"
]
DEFAULT_RESPONSE_PREFERENCE={
            'wsgi.version':         (1, 0),
            'wsgi.url_scheme':      "http",
            'wsgi.input':           "self.rfile",
            'wsgi.errors':          "sys.stderr",
            'wsgi.multithread':     False,
            'wsgi.multiprocess':    False,
            'wsgi.run_once':        False,
            'werkzeug.server.shutdown': None,
            'SERVER_SOFTWARE':      "Webwork",
            'REQUEST_METHOD':       "GET",
            'SCRIPT_NAME':          '',
            'PATH_INFO':            "/",
            'QUERY_STRING':         "",
            'HTTP_HOST':         "127.0.0.1:8080",
            'REMOTE_ADDR':          "127.0.0.1",
            'REMOTE_PORT':          8080,
            'SERVER_NAME':          "localhost",
            'SERVER_PORT':          "8080",
            'SERVER_PROTOCOL':      "HTTP/1.1",
            'OTHERS':{}

  }
