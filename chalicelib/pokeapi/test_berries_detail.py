import pytest
import requests

from . import api


@pytest.fixture
def mock_get_berries_list(monkeypatch):

    def mock_get():
        return ['pecha', 'rawst']
    
    monkeypatch.setattr(api, 'get_berries_list', mock_get)


@pytest.fixture
def mock_requests_get(monkeypatch):

    def mock_get(url):

        class MockResponse:

            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
            
        if url == 'https://pokeapi.co/api/v2/berry/pecha/':
            return MockResponse({'id': 1}, 200)
        elif url == 'https://pokeapi.co/api/v2/berry/rawst/':
            return MockResponse({'id': 2}, 200)
        else:
            return MockResponse(None, 404)
        
    monkeypatch.setattr(requests, 'get', mock_get)


def test_get_berries_detail(mock_get_berries_list, mock_requests_get):

    berries_detail = api.get_berries_detail(api.get_berries_list())

    assert len(berries_detail) == 2
    assert berries_detail[0]['id'] == 1
    assert berries_detail[1]['id'] == 2