
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

    def __get_routes(self, start, end, visited, stops):
        if stops < 0:
            return []
        stops -= 1
        trips = []
        for x in self.routes.get(start, dict()).keys():
            edge = '{}-{}'.format(start, x)
            if x == end:
                # print visited, edge, stops
                trips += [visited + [edge]]
            trips += self.__get_routes(x, end, visited + [edge], stops)
        return trips

    def __get_number_of_routes(self, route, stops, predicate):
        start, end = route.split('-')
        visited = []
        return len([s for s in self.__get_routes(start, end, visited, stops)
                    if predicate(len(s))])

    def get_number_of_routes_with_max_stops(self, route, stops):
        return self.__get_number_of_routes(route, stops, lambda x: x <= stops)

    def get_number_of_routes_with_exact_stops(self, route, stops):
        return self.__get_number_of_routes(route, stops, lambda x: x == stops)

    def get_length_of_the_shortest_route(self, route):
        start, end = route.split('-')
        visited = []
        MAX_STOPS = 10

        def path_length(p):
            start, end = p.split('-')
            return self.routes[start][end]

        def route_length(route):
            return sum(path_length(p) for p in route)

        return min(route_length(r) for r in self.__get_routes(start, end, visited, MAX_STOPS))


def print_distance(route):
    try:
        print setup.get_distance(route)
    except NoSuchRoute:
        print 'NO SUCH ROUTE'


def print_number_of_routes_with_max_stops(route, stops):
    try:
        print setup.get_number_of_routes_with_max_stops(route, stops)
    except NoSuchRoute:
        print 'NO SUCH ROUTE'


def print_number_of_routes_with_exact_stops(route, stops):
    try:
        print setup.get_number_of_routes_with_exact_stops(route, stops)
    except NoSuchRoute:
        print 'NO SUCH ROUTE'


def print_length_of_shortest_route(route):
    try:
        print setup.get_length_of_the_shortest_route(route)
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
    print_number_of_routes_with_max_stops('C-C', 3)
    print_number_of_routes_with_exact_stops('A-C', 4)
    print_length_of_shortest_route('A-C')
    print_length_of_shortest_route('B-B')
