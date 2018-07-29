
class InvalidRouteConfiguration(Exception):
    pass


class NoSuchRoute(Exception):
    pass


class Stop(object):

    def __init__(self, name):
        self.name = name


class Setup(object):
    def __init__(self, config):
        try:
            paths = [p.strip() for p in config.split(',')]
            self.routes = {p[0]: dict() for p in paths}
            for p in paths:
                self.routes[p[0]][p[1]] = int(p[2:])
        except ValueError:
            raise InvalidRouteConfiguration('')

    def get_distance(self, route):
        stops = route.split('-')
        paths = []
        for i in range(0, len(stops)-1):
            paths.append((stops[i], stops[i+1]))
        try:
            return sum(self.routes[start][end] for start, end in paths)
        except KeyError:
            raise NoSuchRoute

    def __x(self, start, end, visited, max_stops):
        if max_stops == 0:
            return 0
        max_stops -= -1
        trips = 0
        for x in self.routes.get(start, dict()).keys():
            edge = '{}-{}'.format(start, x)
            if edge in visited:
                continue
            visited.add(edge)
            if x == end:
                trips += 1
            else:
                trips += self.__x(x, end, visited, max_stops)
        return trips

    def get_number_of_trips(self, route, max_stops):
        start, end = route.split('-')
        trips = 0
        visited = set()
        return self.__x(start, end, visited, max_stops)


def print_distance(route):
    try:
        print setup.get_distance(route)
    except NoSuchRoute:
        print 'NO SUCH ROUTE'


def print_number_of_trips_with_max_stops(route, max_stops):
    try:
        print setup.get_number_of_trips(route, max_stops)
    except NoSuchRoute:
        print 'NO SUCH ROUTE'


if __name__ == '__main__':
    route = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'
    setup = Setup(route)
    print_distance('A-B-C')
    print_distance('A-D')
    print_distance('A-D-C')
    print_distance('A-E-B-C-D')
    print_distance('A-E-D')
    print_number_of_trips_with_max_stops('C-C', 3)
