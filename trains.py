"""
trains.py: A package to provide the route information for trains
"""


class InvalidRouteConfiguration(Exception):
    pass


class NoSuchRoute(Exception):
    pass


class RouteInfo(object):
    def __init__(self, config):
        try:
            paths = [p.strip() for p in config.split(',')]
            self.routes = {p[0]: dict() for p in paths}
            for p in paths:
                self.routes[p[0]][p[1]] = int(p[2:])
        except ValueError:
            raise InvalidRouteConfiguration('')

    def get_route_distance(self, route):
        stops = route.split('-')
        paths = [(stops[i], stops[i+1]) for i in range(0, len(stops)-1)]
        try:
            return sum(self.routes[start][end] for start, end in paths)
        except KeyError:
            raise NoSuchRoute

    def __get_routes(self, start, end, stops=10, visited=()):
        if stops < 0:
            return ()
        stops -= 1
        trips = []
        for x in self.routes.get(start, dict()).keys():
            edge = '{}-{}'.format(start, x)
            new_visited = visited + (edge,)
            if x == end:
                # print visited, edge, stops
                trips += [new_visited]
            trips += self.__get_routes(x, end, stops, new_visited)
        return trips

    def __get_number_of_routes(self, route, stops, predicate):
        start, end = route.split('-')
        return len([s for s in self.__get_routes(start, end, stops)
                    if predicate(len(s))])

    def get_number_of_routes_with_max_stops(self, route, stops):
        return self.__get_number_of_routes(route, stops, lambda x: x <= stops)

    def get_number_of_routes_with_exact_stops(self, route, stops):
        return self.__get_number_of_routes(route, stops, lambda x: x == stops)

    def __get_routes_with_distance(self, route):
        start, end = route.split('-')

        def path_length(p):
            start, end = p.split('-')
            return self.routes[start][end]

        def route_length(route):
            return sum(path_length(p) for p in route)

        return ((r, route_length(r))
                for r in self.__get_routes(start, end))

    def get_length_of_the_shortest_route(self, route):
        return min(l for _, l in self.__get_routes_with_distance(route))

    def get_number_of_different_routes_within_a_distance(self, route, max_distance):
        return len([l for _, l in self.__get_routes_with_distance(route)
                    if l < max_distance])
