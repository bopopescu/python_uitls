import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


class GetDate(object):
    from GetDate import getWeaterDate
    getWeaterDate()


if __name__ == "__main__":
    app = make_app()
    port = 9001
    app.listen(port)
    print 'Server is running in localhost:' + str(port)
    # tornado.ioloop.IOLoop.current().start()

    GetDate()

