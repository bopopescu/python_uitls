

import tornado as tornado
import tornado.web
import tornado.ioloop



class Main():
    def get(self, *args, **kwargs):
        print "test"


application = tornado.web.Application([
    (r"/" , Main ),


])

def runServer():
    port = 9001
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    print "Server is Running in localhost" + port

runServer()