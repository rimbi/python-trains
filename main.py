
class Setup(object):
    def __init__(self, config):
        self.config = config
        self.routes = {'{}-{}'.format(r[0], r[1]): int(r[2:])
                       for r in config.split('-')}

    def get_distance(self, route):
        return self.routes[route]


if __name__ == '__main__':
    print 'Hello, world!'
