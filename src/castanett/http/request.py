
class Request():
    def __init__(self,data,environ):

        self.environ = environ
        self.data = data
        self.content = ''
        self.status = 200

    def setContent(self,content):
        self.content = content
    def setStatus(self,status):
        self.status = status

    def __repr__(self):
        return "<Request>"
