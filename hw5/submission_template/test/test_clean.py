import os
import sys
import unittest
from pathlib import Path

parentdir = Path(__file__).parents[1] #submission_template
sys.path.append(os.path.join(parentdir))
from src import utils

class CleanTest(unittest.TestCase):
    def load_fixture(self, f_name):
        dir=os.path.dirname(__file__)
        fixture_path = os.path.join(dir, "fixtures", f_name)
        posts = utils.open_and_loads(fixture_path)
        return posts

    def setUp(self):
        # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.
        self.fixture1 = self.load_fixture("test_1.json")
        self.fixture2 = self.load_fixture("test_2.json")
        self.fixture3 = self.load_fixture("test_3.json")
        self.fixture4 = self.load_fixture("test_4.json")
        self.fixture5 = self.load_fixture("test_5.json")
        self.fixture6 = self.load_fixture("test_6.json")

    def test_title(self):
        self.assertFalse(utils.check_title_and_replace(self.fixture1[0]))

    def test_datetime(self):
        self.assertFalse(utils.check_datetime(self.fixture2[0]))

    def test_malformed_json(self):
        self.assertEqual(self.fixture3, [])

    def test_author(self):
        self.assertFalse(utils.check_author(self.fixture4[0]))

    def test_total_count(self):
        self.assertFalse(utils.check_total_count(self.fixture5[0]))

    def test_check_tags(self):
        self.assertTrue(utils.check_tags(self.fixture6[0]))

    def test_example_output(self):
        dir = os.path.dirname(os.path.dirname(__file__))
        output_path = os.path.join(dir, "example_output.json")
        posts = utils.open_and_loads(output_path)
        self.assertEqual(posts,
                   [{"title": "First title", "createdAt": "2020-10-19T02:56:51+0000", "text": "Some post content", "author": "druths", "total_count": "12"},
                    {"title": "Third title", "createdAt": "2020-10-17T02:56:51+0900", "text": "Some post content", "author": "druths", "total_count": 22, "tags": ["data", "science", "data", "data", "annotation"]},
                    {"title": "Fourth title", "createdAt": "2020-10-17T02:56:51+0700", "text": "Some post content", "author": "druths", "total_count": 22.9, "tags": ["double", "axel", "spin", "double", "Lutz"]}
                    ])

    def test_more_examples_output(self):
        dir = os.path.dirname(os.path.dirname(__file__))
        output_path = os.path.join(dir, "more_tests_output.json")
        posts = utils.open_and_loads(output_path)
        self.assertEqual(posts,
                         [{"title": "First title", "createdAt": "2020-10-19T02:56:51+0000", "text": "Some post content", "author": "druths", "total_count": "12"},
                          {"title": "Second title", "createAt": "2020-10-19T02:56:51+000", "text": "Some post content", "author": "Claris", "total_count": "10"},
                          {"title": "Third title", "createAt": "2020-10-19T02:56:51+00:00", "text": "Some post content", "author": "Claris", "total_count": 22},
                          {"title": "Fourth title", "createAt": "2020-10-19T02:56:51+0000", "text": "Some post content", "author": "Claris", "total_count": 32.0},
                          {"title": "Sixth title", "createAt": "2020-10-19T02:56:51+0000", "text": "Some post content", "author": "Claris", "total_count": 10, "tags": ["cat", "lover", "dog", "lover"]},
                         ])

if __name__ == '__main__':
    unittest.main()