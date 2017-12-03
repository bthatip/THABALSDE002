'''
This file used for checking the Results obtained from quotes.py. This file has 3 test-cases
- First TestCase(test_json_file_has_ten_elements): Checks for the number of quotes obtained in the JSON file
- Second TestCase(test_author_name_is_mark_twain): Checks for the name of the Author is correct or not
- Third TestCase(test_popular_quotes): Checks for the posts obtained are ordered based on Popularity

Author: Bala Vineeth Netha Thatipamula
'''
import unittest
import json

class TestQuotes(unittest.TestCase):
    # Variable for storing the JSON elements list
    data = json.load(open('quotes.json'))

    ## TESTCASE - for checking number of elements in the JSON File
    def test_json_file_has_ten_elements(self):
        expected_count = 10
        actual_count = len(self.data)
        self.assertEqual(actual_count, expected_count)

    ## TESTCASE - for checking the author name is Mark Twain for all the quotes collected
    def test_author_name_is_mark_twain(self):
        count = 0
        for elem in self.data:
            author_name = elem['author'].lower()
            if(author_name == 'mark twain'):
                count +=1
        #Checking whether all the author names were Mark Twain or not
        self.assertEqual(count, 10)

    ## TESTCASE - For checking the popularity of the quotes
    def test_popular_quotes(self):
        likes = [elem['likes'] for elem in self.data]
        self.assertEqual(likes, sorted(likes, reverse=True))

if __name__ == '__main__':
    unittest.main()
