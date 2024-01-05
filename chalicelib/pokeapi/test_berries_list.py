from unittest.mock import Mock

import pytest
import requests

from .api import get_berries_list


@pytest.fixture
def mock_requests_get(monkeypatch):

    def mock_get(url):

        class MockResponse:

            def __init__(self, json_data, status_code):

                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
            
        if url == 'https://pokeapi.co/api/v2/berry/':
            return MockResponse({
                'results': [{'name': 'cheri'}, {'name': 'chesto'}],
                'next': 'https://pokeapi.co/api/v2/berry/?offset=20&limit=20',
            }, 200)
        elif url == 'https://pokeapi.co/api/v2/berry/?offset=20&limit=20':
            return MockResponse({
                'results': [],
                'next': None,
            }, 200)
        else:
            return MockResponse(None, 404)
        
    monkeypatch.setattr(requests, 'get', mock_get)


def test_get_berries_list(mock_requests_get):
    
    berries = get_berries_list()

    assert len(berries) == 2
    assert berries == ['cheri', 'chesto']