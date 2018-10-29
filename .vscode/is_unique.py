import unittest
import hypothesis
from hypothesis import given, settings
from hypothesis import strategies as st

def check_unique_chars_in_string(string_to_check):
    """returns True if all chars are unique, False otherwise"""
    store = {}
    for i in string_to_check:
        if i in store:
            return False
        
        store[i] = 1

    return True



class TestUniqCharInString(unittest.TestCase):
    @given(test_string = st.text())
    def test_unique_chars_crash(self, test_string):
        check_unique_chars_in_string(test_string)


    @given(test_string = st.from_regex(r"^(.)(?!\1)(.)$"))
    def test_unique_chars_two(self, test_string):
        self.assertTrue(check_unique_chars_in_string(test_string))


    @settings(suppress_health_check = hypothesis.HealthCheck.all())
    @given(test_string = st.from_regex(r"((.)(.)*?(?=\2)(.))+"))
    def test_repeated_char(self, test_string):
        self.assertFalse(check_unique_chars_in_string(test_string))


    def test_unique_string(self):
        self.assertTrue(check_unique_chars_in_string("abcdefghijklmnopqrstuvwxyz"))


    def test_repeated_char_at_end(self):
        self.assertFalse(check_unique_chars_in_string("abcdefghijklmnopqrstuvwxyza"))


    def test_doubled_char_in_string(self):
        self.assertFalse(check_unique_chars_in_string("abcdefghijklmmnopqrstuvwxyz"))


    def test_repeated_char_middles(self):
        self.assertFalse(check_unique_chars_in_string("abcdefghijklmnopqristuvwxyz"))


    def test_caps_differ(self):
        self.assertTrue("abcdefghijklAmnopqrstuvwxyz")


if __name__ == '__main__':
    unittest.main()