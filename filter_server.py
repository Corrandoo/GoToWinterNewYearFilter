import tornado.ioloop
import tornado.web
import os
import uuid

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('upload.html')
    def post(self):
        fileinfo = self.request.files['image'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open('images/' + cname, 'w')
        fh.write(fileinfo['body'])
        #обработка
        fh = open('results/' + cname, 'w')
        fh.write(fileinfo['body'])
        self.render('result.html', name=cname)


settings = [
    ('/', MainHandler),
    ('/images/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ('/results/(.*)', tornado.web.StaticFileHandler, {'path': 'static'})
]

app = tornado.web.Application(settings)
app.listen(80)
tornado.ioloop.IOLoop.current().start()