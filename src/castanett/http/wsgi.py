import socket  # Networking support
import time    # Current time

from castanett.application.reference import HTTP_STATUS_CODES,DEFAULT_RESPONSE_PREFERENCE,REQUEST_METHOD
#https://github.com/pallets/werkzeug/blob/0d6d93e5b545fbb81bd0604d9e13fa4e05eea528/werkzeug/serving.py

class WSGI():
    def __init__(self):
        self.host=None
        self.port=None

        self.www_dir = 'www'
        self.value_environ = DEFAULT_RESPONSE_PREFERENCE
        self.load_view = None


    def address(self,host="0.0.0.0",port=5000):
        self.host=host
        self.port=port


    def activate_server(self,method):
        self.load_view = method
        """ Attempts to aquire the socket and launch the server """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try: # user provided in the __init__() port may be unavaivable
            print("Launching HTTP server on ", self.host, ":",self.port)
            self.socket.bind((self.host, self.port))

        except Exception as e:
            print ("Warning: Could not aquite port:",self.port,"\n")
            print ("I will try a higher port")
            # store to user provideed port locally for later (in case 8080 fails)
            user_port = self.port
            if type(user_port)=='int':
                self.port = self.port+1
            else:
                self.port = 8080

            try:
                print("Launching HTTP server on ", self.host, ":",self.port)
                self.socket.bind((self.host, self.port))

            except Exception as e:
                print("ERROR: Failed to acquire sockets for ports ", user_port, " and 8080. ")
                print("Try running the Server in a privileged user mode.")
                self.shutdown()
                import sys
                sys.exit(1)
        self.value_environ['SERVER_PORT'] = self.port
        self.value_environ['REMOTE_PORT'] = self.port

        print ("Server successfully acquired the socket with port:", self.port)
        print ("Press Ctrl+C to shut down the server and exit.")
        self._wait_for_connections()

    def shutdown(self):
        """ Shut down the server """
        try:
            print("Shutting down the server")
            self.socket.shutdown(socket.SHUT_RDWR)

        except Exception as e:
            print("Warning: could not shut down the socket. Maybe it was already closed?",e)

    def _gen_headers(self,  code):
        """ Generates HTTP response Headers. Ommits the first line! """

        # determine response code
        h = ''
        if code in HTTP_STATUS_CODES:
            h = '%s %s %s\n' % (self.value_environ['SERVER_PROTOCOL'], code, HTTP_STATUS_CODES[code] )


        # write further headers
        current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        h += 'Date: ' + current_date +'\n'
        h += 'Server: Simple-Python-HTTP-Server\n'
        h += 'Connection: close\n\n'  # signal that the conection wil be closed after complting the request

        return h

    def _initialize_server_config(self,str_response=""):
        str_response_split = str_response.split(' ')
        self.value_environ['REQUEST_METHOD'] = str_response_split[0]

        response_content = ' '.join(str_response_split[1:len(str_response_split)])
        split_response_content=response_content.splitlines()

        for i,value in enumerate(split_response_content):
            if i ==0:
                http_val = value.split(" ")
                value_split = http_val[0].split('?')
                self.value_environ['SERVER_PROTOCOL'] = http_val[1]
                self.value_environ['PATH_INFO'] = value_split[0]
                self.value_environ['QUERY_STRING'] = len(value_split)>=2 and value_split[1] or ""
            elif i ==1:
                value_split = value.split(': ')
                self.value_environ['HTTP_HOST'] = value_split[1]

            else:
                value_split = value.split(': ')
                if len(value_split)>1:
                    self.value_environ['OTHERS'][value_split[0]] =value_split[1]

    def _initialize_server_response(self,status,set_header):
        pass
    def _wait_for_connections(self):
        """ Main loop awaiting connections """
        while True:
            print ("Awaiting New connection")
            self.socket.listen(3) # maximum number of queued connections

            conn, addr = self.socket.accept()
            # conn - socket to client
            # addr - clients address

            print("Got connection from:", addr)

            data = conn.recv(1024) #receive data from client
            string = bytes.decode(data) #decode it to string

            request_method = string.split(' ')[0]

            self._initialize_server_config(str_response=string)
            html_content = self.load_view(self.value_environ,self._initialize_server_response)

            if (request_method in REQUEST_METHOD):

                response_headers = self._gen_headers( html_content['status'])

                server_response =  response_headers

                server_response += html_content['content']

                conn.send(server_response.encode())
                print ("Closing connection with client")
                conn.close()

            else:
                print("Unknown HTTP request method:", request_method)
