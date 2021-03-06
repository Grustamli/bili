from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/gadirrustamli/Documents/Projects/bili/backend/bili/functional_tests/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
