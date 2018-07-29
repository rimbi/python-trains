from expects import expect, be, raise_error
from main import Setup, InvalidRouteConfiguration, NoSuchRoute


def test_setup_should_work_with_single_route_info():
    # given
    setup = Setup('AB5')
    # when
    distance = setup.get_distance('A-B')
    # then
    expect(distance).to(be(5))


def test_setup_should_work_with_multiple_route_info():
    # given
    setup = Setup('AB5-CD4-DE6')
    # when
    distance = setup.get_distance('C-D')
    # then
    expect(distance).to(be(4))


def test_setup_should_raise_exception_when_invalid_route_configuration_provided():
    # given
    # when
    def call(): return Setup('AB5-C4D-DE6')
    # then
    expect(call).to(raise_error(InvalidRouteConfiguration))


def test_setup_should_raise_no_such_route_for_invalid_route_query():
    # given
    setup = Setup('AB5-CD4-DE6')
    # when

    def call(): return setup.get_distance('A-C')
    # then
    expect(call).to(raise_error(NoSuchRoute))
