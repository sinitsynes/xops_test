import json
from fastapi.testclient import TestClient

import pytest

from main import app
from app.db.connection import get_test_session, get_session


@pytest.fixture
def test_client(request):
    app.dependency_overrides[get_session] = get_test_session
    client = TestClient(app)
    return client


@pytest.fixture
def good_links():
    return json.dumps({"links":["https://ya.ru/",
                                "https://ya.ru/search/?text=мемы+с+котиками",
                                "https://sber.ru",
                                "https://stackoverflow.com/questions/65724760/how-it-is"]})


@pytest.fixture
def good_status():
    return {'status':'ok'}


@pytest.fixture
def bad_links():
    return json.dumps({"links":[1,2,3,4]})


@pytest.fixture
def bad_request():
    return json.dumps({"bad_key": [1,2,3,4]})


@pytest.fixture
def good_visited_domains_response():
    return ["stackoverflow.com", "ya.ru", "sber.ru"]
