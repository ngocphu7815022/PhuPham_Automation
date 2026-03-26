import pytest

@pytest.mark.regression
@pytest.mark.slow
@pytest.mark.ui
def test_payment_by_credit_card():
    assert True

@pytest.mark.sanity
@pytest.mark.ui
def test_payment_by_cash():
    assert True
