import SimpleHTTPServer
import SocketServer
from multiprocessing import Process
from os import listdir
from settings import constants
import time


def get_file_names(path):
    file_names = [f for f in listdir(path)
                  if any([
                    f.endswith(".js"),
                    f.endswith(".html"),
                    f.endswith(".css")]) and
                  not f.startswith("compiled_")]
    return file_names


def compile_lib():
    path = "lib"
    for f in get_file_names(path):
        file_path = "%s/%s" % (path, f)
        with open(file_path, 'r') as fp:
            content = fp.read()
            for constant, value in constants.iteritems():
                content = content.replace("@(%s)" % constant, value)
        new_file = "%s/compiled_%s" % (path, f)
        with open(new_file, 'w') as fp:
            fp.write(content)


def get_file_dict():
    path = "lib"
    files = {}
    for f in get_file_names(path):
        file_path = "%s/%s" % (path, f)
        with open(file_path, 'r') as fp:
            files[file_path] = fp.read()
    return files


def listen_for_changes(name):
    files = get_file_dict()
    while True:
        time.sleep(2)
        new_files = get_file_dict()
        if files != new_files:
            compile_lib()
            files = new_files


def serve():
    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "Serving at port:", PORT
    httpd.serve_forever()

compile_lib()
p = Process(target=listen_for_changes, args=('bob',))
p.start()
serve()
