#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()


import os
from psycogreen.gevent import patch_psycopg



import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socketioapp.settings")
    patch_psycopg()

	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()    


    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



    from socketio.server import SocketIOServer
    server = SocketIOServer(('', 8000), application, resource="socket.io")
    server.serve_forever()
