
def expect_true(value):
    if value:
        print("PASS")
    else:
        raise ValueError("Test failed")

def expect_false(value):
    if not value:
        print("PASS")
    else:
        raise ValueError("Test failed")

def expect_equal(value, expected_value):
    if value == expected_value:
        print("PASS")
    else:
        print(value)
        print(expected_value)
        raise ValueError("Test failed")

def expect_different(value, expected_value):
    if value != expected_value:
        print("PASS")
    else:
        raise ValueError("Test failed")
    