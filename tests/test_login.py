import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_login_success():
    assert True

@pytest.mark.regression
@pytest.mark.ui
def test_login_wrong_password():
    assert True
