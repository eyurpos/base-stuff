from anagram import is_anagram
from stest import (expect_true, expect_false)

test_string_1 = "restful"
test_string_2 = "restdul"
test_anagram = "fluster"

expect_true(is_anagram(test_string_1, test_anagram))
expect_false(is_anagram(test_string_2, test_anagram))
