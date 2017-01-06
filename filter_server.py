import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('upload.html')

settings = [
    ('/', MainHandler),
    ('/images/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ('/results/(.*)', tornado.web.StaticFileHandler, {'path': 'static'})
]

app = tornado.web.Application(settings)
app.listen(80)
tornado.ioloop.IOLoop.current().start()