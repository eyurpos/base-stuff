from is_palindrome import is_palindrome
from stest import (expect_true, expect_false)

expect_true(is_palindrome("a"))
expect_true(is_palindrome("aa"))
expect_false(is_palindrome("ab"))
expect_true(is_palindrome("aaabaaa"))
expect_true(is_palindrome("aaabbaaa"))
expect_false(is_palindrome("aaabcaaa"))
