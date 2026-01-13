# server/testing/test_app.py
import pytest
from app import create_app, db
from models import User

@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # seed data
            user = User(username="testuser")
            db.session.add(user)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Hello, world!" in resp.data

def test_users(client):
    resp = client.get('/users')
    assert resp.status_code == 200
    assert b"testuser" in resp.data
