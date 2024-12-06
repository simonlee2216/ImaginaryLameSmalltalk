import pytest
from app import app  

def test_example():
    response = app.test_client().get('/')
    assert response.status_code == 200
