from expects import expect, be, raise_error
from trains import RouteInfo, InvalidRouteConfiguration, NoSuchRoute


def test_setup_should_work_with_single_route_info():
    # given
    setup = RouteInfo('AB5')
    # when
    distance = setup.get_distance('A-B')
    # then
    expect(distance).to(be(5))


def test_setup_should_work_with_multiple_route_info():
    # given
    setup = RouteInfo('AB5, CD4, DE6')
    # when
    distance = setup.get_distance('C-D')
    # then
    expect(distance).to(be(4))


def test_setup_should_raise_exception_when_invalid_route_configuration_provided():
    # given
    # when
    def call(): return RouteInfo('AB5, C4D, DE6')
    # then
    expect(call).to(raise_error(InvalidRouteConfiguration))


def test_setup_should_raise_no_such_route_for_invalid_route_query():
    # given
    setup = RouteInfo('AB5, CD4, DE6')
    # when

    def call(): return setup.get_distance('A-C')
    # then
    expect(call).to(raise_error(NoSuchRoute))


def test_setup_should_compute_routes_with_single_stop():
    # given
    setup = RouteInfo('AB5, BC4, CD6')
    # when
    distance = setup.get_distance('A-B-C')
    # then
    expect(distance).to(be(9))


def test_setup_should_compute_routes_with_multiple_stops():
    # given
    setup = RouteInfo('AB5, BC4, CD6')
    # when
    distance = setup.get_distance('A-B-C-D')
    # then
    expect(distance).to(be(15))


def test_setup_should_compute_number_of_trips_with_max_stops_1():
    # given
    setup = RouteInfo('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    # when
    routes = setup.get_number_of_routes_with_max_stops('C-C', 3)
    # then
    expect(routes).to(be(2))


def test_setup_should_compute_number_of_trips_with_exact_stops_1():
    # given
    setup = RouteInfo('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    # when
    routes = setup.get_number_of_routes_with_exact_stops('A-C', 4)
    # then
    expect(routes).to(be(3))


def test_setup_should_compute_length_of_the_shortest_route_1():
    # given
    setup = RouteInfo('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    # when
    length = setup.get_length_of_the_shortest_route('A-C')
    # then
    expect(length).to(be(9))


def test_setup_should_compute_length_of_the_shortest_route_1():
    # given
    setup = RouteInfo('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    # when
    length = setup.get_length_of_the_shortest_route('B-B')
    # then
    expect(length).to(be(9))


def test_setup_should_compute_the_number_of_different_routes():
    # given
    setup = RouteInfo('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
    # when
    length = setup.get_number_of_different_routes_within_a_distance('C-C', 30)
    # then
    expect(length).to(be(7))
