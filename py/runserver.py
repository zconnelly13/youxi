from os import listdir
import SimpleHTTPServer
from settings import constants
import SocketServer


def compile_lib():
    path = "lib"
    file_names = [f for f in listdir(path)
                  if any([
                    f.endswith(".js"),
                    f.endswith(".html"),
                    f.endswith(".css")]) and
                  not f.startswith("compiled_")]
    for f in file_names:
        file_path = "%s/%s" % (path, f)
        with open(file_path, 'r') as fp:
            content = fp.read()
            for constant, value in constants.iteritems():
                content = content.replace("@(%s)" % constant, value)
        new_file = "%s/compiled_%s" % (path, f)
        with open(new_file, 'w') as fp:
            fp.write(content)


def serve():
    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "Serving at port:", PORT
    httpd.serve_forever()

compile_lib()
serve()
