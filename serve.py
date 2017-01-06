#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

PORT = 1334

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port %r" % PORT

httpd.serve_forever()