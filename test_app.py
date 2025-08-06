
import app

def test_hello():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_404():
    client = app.app.test_client()
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_content_type():
    client = app.app.test_client()
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'
