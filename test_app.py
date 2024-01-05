import pytest

from chalicelib.pokeapi import api
from app import fetch_growth_time_stats_from_api


@pytest.fixture
def mock_get_berries_list(monkeypatch):

    def mock_get():
        return ['leppa', 'oran', 'persim']
    
    monkeypatch.setattr(api, 'get_berries_list', mock_get)


@pytest.fixture
def mock_get_berries_detail(monkeypatch):

    def mock_get(berries_names: list[str]):
        return [
            {'growth_time': 1},
            {'growth_time': 2},
            {'growth_time': 3}
        ]

    monkeypatch.setattr(api, 'get_berries_detail', mock_get)


def test_get_growth_time_stats(mock_get_berries_list, mock_get_berries_detail):

    res = fetch_growth_time_stats_from_api()

    assert res == {
        "berries_names": ['leppa', 'oran', 'persim'],
        "min_growth_time": 1.0,
        "median_growth_time": 2.0,
        "max_growth_time": 3.0,
        "variance_growth_time": 1,
        "mean_growth_time": 2.0,
        "frequency_growth_time": {1: 1, 2: 1, 3: 1}
    }