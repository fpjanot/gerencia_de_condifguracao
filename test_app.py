from app import app

def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, World!'
