
class InvalidRouteConfiguration(Exception):
    pass


class NoSuchRoute(Exception):
    pass


class Setup(object):
    def __init__(self, config):
        try:
            self.routes = {'{}-{}'.format(r[0], r[1]): int(r[2:])
                           for r in config.split('-')}
        except ValueError:
            raise InvalidRouteConfiguration('')

    def get_distance(self, route):
        try:
            return self.routes[route]
        except KeyError:
            raise NoSuchRoute


if __name__ == '__main__':
    print 'Hello, world!'
