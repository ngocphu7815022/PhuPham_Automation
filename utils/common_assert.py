def assert_equal(actual, expected, field_name=""):
    assert (
        actual == expected
    ), f"[{field_name}] Expected '{expected}', but got '{actual}'"
