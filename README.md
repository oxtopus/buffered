Simple demonstration of streaming with nginx, uwsgi, and web.py.  The trick is 
in the X-Accel-Buffering header and generators.

## Start services
    
    $ make
    $ nginx -p . -c conf/nginx.conf
    $ uwsgi --ini conf/uwsgi.ini

## Make requests

    curl -N http://localhost:8080
