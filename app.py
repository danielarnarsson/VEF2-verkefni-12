import bottle, os

@bottle.route('/')
def test():
    return 'Test'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    bottle.run(host='0.0.0.0', port=argv[1])
