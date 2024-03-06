import pytest
from fastapi.testclient import TestClient
from my_module import add, multiply  # Assuming my_module contains your functions

# Assuming you have a FastAPI app named 'app' as in your code
from myfastapi import app  # Replace 'main' with the actual name of your main FastAPI module

@pytest.fixture
def test_client():
    return TestClient(app)

def test_get_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the default payment risk prediction API'}

def test_get_customer_id(test_client):
    response = test_client.get("/customer/123")
    assert response.status_code == 200
    assert 'id_client' in response.json()

def test_get_prediction(test_client):
    response = test_client.get("/prediction?sk_id_cust=123")
    assert response.status_code == 200
    assert 'prediction' in response.json()
    assert 'prediction_explanation' in response.json()

# Add more tests as needed
