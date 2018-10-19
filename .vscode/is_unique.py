import unittest
import hypothesis
from hypothesis import given
from hypothesis import strategies as st

def check_unique_chars_in_string(string_to_check):
    """returns True if all chars are unique, False otherwise"""
    for i in range(len(string_to_check)):
        if check_matches_char_in_str(string_to_check[i], string_to_check[i+1:]):  # check whether i occurs later in string_to_check returned true? 
            return False
    else:
        return True


def check_matches_char_in_str(target_character, match_string):
    for i in match_string:
        if target_character == i:
            return True

    
    return False  # exited for loop without finding another occurence of target_character


class TestUniqCharInString(unittest.TestCase):
    @given(test_string = st.text())
    def test_unique_chars_crash(self, test_string):
        check_unique_chars_in_string(test_string)


    def test_unique_string(self):
        self.assertTrue(check_unique_chars_in_string("abcdefghijklmnopqrstuvwxyz"))


    def test_repeated_char_at_end(self):
        self.assertFalse(check_unique_chars_in_string("abcdefghijklmnopqrstuvwxyza"))


    def test_doubled_char_in_string(self):
        self.assertFalse(check_unique_chars_in_string("abcdefghijklmmnopqrstuvwxyz"))


    def test_repeated_char_middles(self):
        self.assertFalse(check_unique_chars_in_string("abcdefghijklmnopqristuvwxyz"))


if __name__ == '__main__':
    unittest.main()