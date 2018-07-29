from expects import expect, be
from main import Setup

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
