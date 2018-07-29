"""
trains.py: A package to provide the route information for trains
"""


class InvalidRouteConfiguration(Exception):
    pass


class NoSuchRoute(Exception):
    pass


class RouteInfo(object):
    """
    A class for doing route calculations
    """

    def __init__(self, config):
        try:
            paths = [p.strip() for p in config.split(',')]
            self.routes = dict()
            for p in paths:
                self.routes.setdefault(p[0], dict())[p[1]] = int(p[2:])
        except ValueError:
            raise InvalidRouteConfiguration('')

    def get_route_distance(self, route):
        """
        Returns total direct distance within route.
        This calculation use only the distances between stops in the route
        """
        stops = route.split('-')
        paths = [(stops[i], stops[i+1]) for i in range(0, len(stops)-1)]
        try:
            return sum(self.routes[start][end] for start, end in paths)
        except KeyError:
            raise NoSuchRoute

    def __get_routes(self, start, end, stops=10, visited=()):
        """
        Returns all possible unique routes between <start> and <end> up to <stops>.
        Ex:
        Input: ('A', 'E', 3) 
        Output: [('A-B', 'B-E'), ('A-B', 'B-C', C-E')]
        """
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
        """
        Given a <route> in the format Start-End, retuens the number of
        different routes within <stops> and holds <predicate>
        """
        start, end = route.split('-')
        return len([s for s in self.__get_routes(start, end, stops)
                    if predicate(len(s))])

    def get_number_of_routes_with_max_stops(self, route, stops):
        """
        Given a <route> in the format Start-End, retuens the number of
        different routes within <stops>
        """
        return self.__get_number_of_routes(route, stops, lambda x: x <= stops)

    def get_number_of_routes_with_exact_stops(self, route, stops):
        """
        Given a <route> in the format Start-End, finds the number of
        different routes within <stops> and returns only the ones with exactly <stops>
        """
        return self.__get_number_of_routes(route, stops, lambda x: x == stops)

    def __get_routes_with_distance(self, route):
        """
        Given a <route> in the format Start-End, returns all possible 
        unique routes with their distances
        Ex output: [(('A-B', 'B-C'), 9)]
        """
        start, end = route.split('-')

        def path_length(p):
            start, end = p.split('-')
            return self.routes[start][end]

        def route_length(route):
            return sum(path_length(p) for p in route)

        return ((r, route_length(r))
                for r in self.__get_routes(start, end))

    def get_length_of_the_shortest_route(self, route):
        """
        Given a <route> in the format Start-End, 
        returns the length of the shortest route
        """
        return min(l for _, l in self.__get_routes_with_distance(route))

    def get_number_of_different_routes_within_a_distance(self, route, max_distance):
        """
        Given a <route> in the format Start-End and a <max_distance>, 
        returns the number of different routes with distance less than <max_distance>
        """
        return len([l for _, l in self.__get_routes_with_distance(route)
                    if l < max_distance])
