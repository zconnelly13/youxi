from os import listdir
from settings import constants


def compile_lib():
    path = "../lib"
    file_names = [f for f in listdir(path)
                  if any([
                    f.endswith(".js"),
                    f.endswith(".html"),
                    f.endswith(".css")])]
    for f in file_names:
        file_path = "%s/%s" % (path, f)
        with open(file_path, 'r') as fp:
            content = fp.readlines()
            for constant, value in constants.iteritems():
                content = content.replace(constant, value)
        new_file = "%s/compiled_%s" % (path, f)
        with open(new_file, 'w') as fp:
            fp.write(content)
    print file_names
    print constants

compile_lib()
