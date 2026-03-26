import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_search_valid_keyword():
    assert True

@pytest.mark.regression
@pytest.mark.slow
@pytest.mark.ui
def test_search_many_results():
    assert True
