import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_calculate_addition(client):
    response = client.post('/calculate', json={'expression': '2+3'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 5


def test_calculate_subtraction(client):
    response = client.post('/calculate', json={'expression': '10-4'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 6


def test_calculate_multiplication(client):
    response = client.post('/calculate', json={'expression': '3*4'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 12


def test_calculate_division(client):
    response = client.post('/calculate', json={'expression': '8/2'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 4.0


def test_calculate_invalid(client):
    response = client.post('/calculate', json={'expression': 'invalid'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 'Error'
