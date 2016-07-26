#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import subprocess

# Set IP to your machine IP
IP = '0.0.0.0'
# Default port
PORT = 2700

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/lazymode':
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      self.wfile.write("Shutting Down...")
      subprocess.call(('shutdown', '-h', 'now'))
    return

def main():
  Handler = RequestHandler
  print 'Starting on port %s' % PORT
  server = SocketServer.TCPServer((IP, PORT), Handler)
  server.serve_forever()

if __name__ == '__main__':
  main()
