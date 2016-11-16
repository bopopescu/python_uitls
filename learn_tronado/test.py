import tornado.ioloop
import tornado.web
import tornado.websocket
# import uimodules as md
# import uimethods as mt

class ParentRequestHandler(tornado.web.RequestHandler):
    def showInfo(self):
        print("ip:", self.request.remote_ip)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class MainHandler2(tornado.web.RequestHandler):
    def get(self):
        self.write("This is a test")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print( "WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print ("WebSocket closed")

class Test(ParentRequestHandler):
    def get(self):
        ParentRequestHandler.showInfo(self)
        self.write(self.get_argument("a"))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/test", MainHandler2),
    (r"/websocket", EchoWebSocket),
    (r"/tag", Test),
])

if __name__ == "__main__":
    port =  8888
    application.listen(port)
    print("run in " , port)
    tornado.ioloop.IOLoop.instance().start()