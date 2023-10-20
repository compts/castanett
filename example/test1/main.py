from castanett.webserver import Webserver
from castanett.routes import Routes

def index(request):
	print("*******************************")
	#print(environ)
	print("*******************************")
	request.setContent("Hello index")
	return request

def post(request):
	html = """
<html>
<body>
   <form method="post" action="" enctype='multipart/form-data'>
        <p>
      
        </p>
        <p>
            Hobbies:
            <input
                name="hobbies" type="checkbox" value="software"
                %(checked-software)s
            > Software
            <input
                name="hobbies" type="checkbox" value="tunning"
                %(checked-tunning)s
            > Auto Tunning
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
       
    </p>
</body>
</html>
"""
	print("*******************************")
	#print(environ)
	print("*******************************")
	#return "index"
	request.setContent(html)
	return request

def error_404():
	return "error:404"

class home():
    
    def index(self,request):
        request.setContent("home:Index")
        return request
    def test(self,request):
        request.setContent("home:test")
        return request

rts = Routes()
rts.error(404,error_404)
rts.url("/",index)
rts.url("/post/",post)
rts.url("/home/index",home().index);

app = Webserver()
app.setDefaultConfig({})
app.setDefaultRoute(rts)
app.run(host="localhost",port=4041);

