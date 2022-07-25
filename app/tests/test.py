import pytest
from app import app
from flask import json
import sqlite3

@pytest.fixture
def setup_database():
    connection = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    connection.commit()
    connection.close()


def test_books():        
    response = app.test_client().get('/books/')
    assert response.status_code == 200

def test_books_by_name():        
    response = app.test_client().get('/books_name/adventures/')
    assert response.status_code == 200

def test_books_by_name_and_with_pagination():        
    response = app.test_client().get('/books_name/adventures/2')
    assert response.status_code == 200
