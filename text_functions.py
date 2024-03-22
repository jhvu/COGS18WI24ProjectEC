import pytest

from functions import find_daily_temp, calculate_crochet_gauge, calculate_blanket_size, yarn_color


@pytest.fixture
def stitches():
    return 15

@pytest.fixture
def rows():
    return 9

@pytest.fixture
def measurement_unit():
    return 'inches'

def test_calculate_crochet_gauge(stitches, rows, measurement_unit):
    assert callable(calculate_crochet_gauge)
    assert type(calculate_crochet_gauge(15, 9, 'inches')) == tuple
    assert calculate_crochet_gauge(20, 4, 'inches') == (5.0, 1.0)
    assert calculate_crochet_gauge(15, 9, 'cm') == None
    
    
@pytest.fixture
def width():
    return 65

@pytest.fixture
def length():
    return 90

@pytest.fixture
def stitch_gauge():
    return 15

@pytest.fixture
def row_gauge():
    return 9
    
def test_calculate_blanket_size(width, length, stitch_gauge, row_gauge):
    assert callable(calculate_blanket_size)
    total_stitches, total_rows = calculate_blanket_size(width, length, stitch_gauge, 
    row_gauge)
    assert total_stitches == 975
    assert total_rows == 810
    
    
@pytest.fixture
def temperature():
    return 31
    
def test_yarn_color(temperature):
    assert callable(yarn_color)
    assert type(yarn_color(31)) == str
    assert yarn_color(31) == 'light blue'
    assert yarn_color(50) == 'green'
