import pytest

from .growth_time import GrowthTimeStats


def test_get_min():

    # unordered
    stats = GrowthTimeStats([7,4,1,5,9,3])
    assert stats.get_min() == 1

    # single element
    stats = GrowthTimeStats([7])
    assert stats.get_min() == 7

    # duplicated
    stats = GrowthTimeStats([3,1,1])
    assert stats.get_min() == 1


def test_get_max():

    # unordered
    stats = GrowthTimeStats([7,4,1,5,9,3])
    assert stats.get_max() == 9

    # single element
    stats = GrowthTimeStats([7])
    assert stats.get_max() == 7

    # duplicated
    stats = GrowthTimeStats([3,1,1])
    assert stats.get_max() == 3


def test_get_mean():

    # unordered
    stats = GrowthTimeStats([7,4,1,5,9,3])
    assert stats.get_mean() == 4.83

    # single element
    stats = GrowthTimeStats([7])
    assert stats.get_mean() == 7

    # duplicated
    stats = GrowthTimeStats([3,1,1])
    assert stats.get_mean() == 1.67

    # all the same
    stats = GrowthTimeStats([1,1,1])
    assert stats.get_mean() == 1


def test_get_median():

    # odd number
    stats = GrowthTimeStats([7,4,1,5,9,3])
    assert stats.get_median() == 4.5

    # even number
    stats = GrowthTimeStats([7,4,1,5,9,3,2])
    assert stats.get_median() == 4

    # duplicated
    stats = GrowthTimeStats([3,1,1])
    assert stats.get_median() == 1

    # all the same
    stats = GrowthTimeStats([1,1,1])
    assert stats.get_median() == 1

    # all the same, even
    stats = GrowthTimeStats([1,1])
    assert stats.get_median() == 1


def test_get_variance():

    # odd number
    stats = GrowthTimeStats([7,4,1,5,9,3])
    assert stats.get_variance() == 8.17

    # even number
    stats = GrowthTimeStats([7,4,1,5,9,2])
    assert stats.get_variance() == 9.07

    # duplicated
    stats = GrowthTimeStats([3,1,1])
    assert stats.get_variance() == 1.33

    # all the same
    stats = GrowthTimeStats([1,1,1])
    assert stats.get_variance() == 0


def test_get_frequency():

    # all different
    stats = GrowthTimeStats([7,4,1,5])
    assert stats.get_frequency() == {
        7: 1,
        4: 1,
        1: 1,
        5: 1
    }

    # all the same
    stats = GrowthTimeStats([7,7,7,7,7])
    assert stats.get_frequency() == {7: 5}

    # some are repeted
    stats = GrowthTimeStats([3,1,1])
    assert stats.get_frequency() == {3: 1, 1: 2}