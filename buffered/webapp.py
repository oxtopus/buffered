import web
from time import sleep

urls = (
  '/*', 'hello'
)

app = web.application(urls, globals())
application = app.wsgifunc()

class hello:        
  def GET(self,):
    web.header('X-Accel-Buffering', 'no')
    for x in xrange(10):
      sleep(1)
      yield "Hello, attempt %d\n" % x

if __name__ == '__main__':
  app.run()