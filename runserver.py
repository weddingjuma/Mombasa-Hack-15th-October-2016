import os
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

from app import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.config['DEBUG'] = True
    app.config['use_reloader'] = True
    app.config['threaded'] = True
    print 'Awesome running at - ' + str(port)

    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
