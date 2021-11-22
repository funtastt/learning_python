import unittest
from function import get_formatted_name

"""
def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()
"""


class NamesTest(unittest.TestCase):
    def test_result(self):
        self.assertEqual(get_formatted_name('name', 'surname'), "Name Surname")


# Вот так работает:
if __name__ == '__main__':
    unittest.main()

# А вот так нет, почему?
# unittest.main()
