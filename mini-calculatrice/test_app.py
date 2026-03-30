import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route returns 200 and contains calculator elements."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'calculator' in rv.data.lower()

def test_calculate_addition(client):
    """Test basic addition calculation."""
    rv = client.post('/calculate', json={'expression': '2+3'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 5

def test_calculate_subtraction(client):
    """Test basic subtraction calculation."""
    rv = client.post('/calculate', json={'expression': '10-4'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 6

def test_calculate_multiplication(client):
    """Test basic multiplication calculation."""
    rv = client.post('/calculate', json={'expression': '3*4'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 12

def test_calculate_division(client):
    """Test basic division calculation."""
    rv = client.post('/calculate', json={'expression': '8/2'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 4.0

def test_calculate_complex_expression(client):
    """Test complex expression with parentheses."""
    rv = client.post('/calculate', json={'expression': '(2+3)*4'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 20

def test_calculate_invalid_expression(client):
    """Test invalid expression returns Error."""
    rv = client.post('/calculate', json={'expression': 'invalid'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 'Error'

def test_calculate_empty_expression(client):
    """Test empty expression."""
    rv = client.post('/calculate', json={'expression': ''})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['result'] == 'Error'