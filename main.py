
class InvalidRouteConfiguration(Exception):
    pass


class NoSuchRoute(Exception):
    pass


class Setup(object):
    def __init__(self, config):
        try:
            self.routes = {'{}-{}'.format(r.strip()[0], r.strip()[1]): int(r.strip()[2:])
                           for r in config.split(',')}
        except ValueError:
            raise InvalidRouteConfiguration('')

    def get_distance(self, route):
        stops = route.split('-')
        paths = []
        for i in range(0, len(stops)-1):
            paths.append('{}-{}'.format(stops[i], stops[i+1]))
        try:
            return sum(self.routes[p] for p in paths)
        except KeyError:
            raise NoSuchRoute


if __name__ == '__main__':
    print 'Hello, world!'
