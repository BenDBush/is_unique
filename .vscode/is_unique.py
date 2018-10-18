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
    def test_unique_chars(self, test_string):
        check_unique_chars_in_string(test_string)

if __name__ == '__main__':
    unittest.main()