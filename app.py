import bottle
from sys import argv

@bottle.route('/')
def test():
    return 'Test'


if __name__ == "__main__":
    bottle.run(host='0.0.0.0', port=argv[1])
