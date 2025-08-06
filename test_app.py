

import app

import pytest

@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_hello_post_method_not_allowed(client):
    response = client.post('/')
    assert response.status_code == 405

def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_content_type(client):
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

def test_headers(client):
    response = client.get('/')
    assert 'Content-Type' in response.headers
