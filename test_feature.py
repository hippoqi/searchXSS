import pytest, os 

from app import app as flask_app, sample_sum_func, sample_sub_func
@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_sum_noInput():
    result = sample_sum_func()
    assert result == 0

def test_sum_withInput():
    result = sample_sum_func(a=1, b=3)
    assert result == 4

def test_sample_sub_func():
    result = sample_sub_func(a=4, b=3)
    assert result == 1