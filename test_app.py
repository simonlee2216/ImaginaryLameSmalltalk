import pytest
from main import app  

def test_example():
    response = app.test_client().get('/')
    assert response.status_code == 200
