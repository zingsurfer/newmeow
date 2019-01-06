import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    def tearDown(self):
        self.browser.quit()
    def test_can_view_home_page(self):
        self.browser.get('http://localhost:8080')
        self.assertIn('NewMeow', self.browser.title)
        # fail regardless until test is finished being written
        self.fail('Is this test finished being written?')

# if this file is executed from CLI, launch unittest to run tests
if __name__ == '__main__':
    unittest.main()
