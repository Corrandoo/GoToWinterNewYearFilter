import tornado.ioloop
import tornado.web
import os
import uuid

from os import listdir

from IPython.core import logger

from filter import processik, processdb, processym, processvc, processmm1, processmm2, processmn

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('c', 'default')
        full_name = ""
        if name=='default':
            newname = str(uuid.uuid4())
            self.render('upload.html', name=newname, error_report = "")
        else:
            list = listdir('results')
            for filename in list:
                if filename.find(name) != -1:
                    full_name = filename

            self.render('result.html', name=full_name) #full name - полное имя файла
    def post(self):
        try:
            name = self.get_argument('c', 'default')
            fileinfo = self.request.files['image'][0]
            fname = fileinfo['filename']
            extn = os.path.splitext(fname)[1]
            cname = name + extn
            fh = open('images/' + cname, 'wb')
            fh.write(fileinfo['body'])
            #обработка

            type = self.get_argument('filter', "default")
            if type == "filterik":
                processik('images/' + cname, 'results/' + cname)
            elif type == "filterym":
                processym('images/' + cname, 'results/' + cname)
            elif type == "filterdb":
                processdb('images/' + cname, 'results/' + cname)
            elif type == "filtervc":
                processvc('images/' + cname, 'results/' + cname)
            elif type == "filtermm1":
                processmm1('images/' + cname, 'results/' + cname)
            elif type == "filtermm2":
                processmm2('images/' + cname, 'results/' + cname)
            elif type == "filtermn":
                processmn('images/' + cname, 'results/' + cname)

            self.render('result.html', name=cname)
        except Exception as e:
            self.render('upload.html', name=str(uuid.uuid4()), error_report="Загрузите фотографию перед ее отправкой в фильтр!")
            print(str(e))


settings = [
    ('/', MainHandler),
    ('/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'}),
    ('/results/(.*)', tornado.web.StaticFileHandler, {'path': 'results'}),
    ('/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    ('/css/(.*)', tornado.web.StaticFileHandler, {'path': 'css'})
]

app = tornado.web.Application(settings)
app.listen(80)
tornado.ioloop.IOLoop.current().start()