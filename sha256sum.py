import hashlib
from sys import argv


def sha256filehash(filename):
    with open(filename, 'rb') as filehandle:
        filebuf = filehandle.read()
        hashret = hashlib.sha256(filebuf).hexdigest()
        print "SHA256:%s : %s" % (hashret, filename)
        filehandle.close()


def main():
    if len(argv) != 2:
        print "This script takes 1 argument. Usage: sha256sum.py path\\to\\file"
        exit(0)
    (scriptname, filename) = argv
    sha256filehash(filename)


if __name__ == '__main__':
        main()
