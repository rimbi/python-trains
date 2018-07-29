#!/usr/bin/env python

"""main.py: Executes test input and prints results."""

from trains import RouteInfo, NoSuchRoute, InvalidRouteConfiguration


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


def print_number_of_different_routes_within_a_distance(route, distance):
    try:
        print setup.get_number_of_different_routes_within_a_distance(
            route, distance)
    except NoSuchRoute:
        print 'NO SUCH ROUTE'


if __name__ == '__main__':
    route = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'
    setup = RouteInfo(route)
    print_distance('A-B-C')
    print_distance('A-D')
    print_distance('A-D-C')
    print_distance('A-E-B-C-D')
    print_distance('A-E-D')
    print_number_of_routes_with_max_stops('C-C', 3)
    print_number_of_routes_with_exact_stops('A-C', 4)
    print_length_of_shortest_route('A-C')
    print_length_of_shortest_route('B-B')
    print_number_of_different_routes_within_a_distance('C-C', 30)
