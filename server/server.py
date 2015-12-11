#!/usr/bin/env python

def main(CMD='make -j', PORT='16280'):
    PORT = int(PORT)

    from BaseHTTPServer import BaseHTTPRequestHandler
    from SocketServer import TCPServer
    from sys import stderr

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            from subprocess import Popen
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            p = Popen(CMD, shell=True, stdout=self.wfile, stderr=self.wfile)
            p.wait()

        def log_message(self, format, *args):
            from time import strftime
            print >> stderr, strftime('%H:%M:%S'), '+', CMD
            return

    print >> stderr, "Starting build server."
    print >> stderr, "Visiting port %d will run: %s" % (PORT, CMD)
    try:
        TCPServer(('', PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        pass
    print >> stderr, "Stopping build server."

if __name__ == '__main__':
    from sys import argv
    main(*argv[1:])
