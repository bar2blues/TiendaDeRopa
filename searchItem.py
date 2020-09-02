import unittest
from selenium import webdriver
from Pages.pageIndex import PageIndex
from Pages.pageItems import PageItem
from Pages.pageItemElement import PageItemElement
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized") # inicia con la ventana maximizada
        option.add_argument("incognito") # sesion de incognito
        option.add_argument('--headless')  # no levanta el browser
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemPage = PageItem(self.driver)
        self.itemElementPage = PageItemElement(self.driver)
        self.driver.implicitly_wait(5)

    #@unittest.skip("Not now")
    def test_search_no_elements(self):
        try:
            self.indexPage.search('hola')
            self.assertEqual(self.itemPage.return_no_element_text(),
                             'No results were found for your search "hola"')
            self.driver.save_screenshot('no_element.jpg')
        except:
            self.driver.save_screenshot("error.jpg")

    #@unittest.skip("Not now")
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemPage.return_section_title())

    #@unittest.skip("Not now")
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.itemPage.return_section_title())

    #@unittest.skip("Not now") # test falla
    def test_add_tshirt_shopcar(self):
        self.indexPage.search('t-shirt')
        self.itemPage.click_orange_button()
        self.itemElementPage.enter_quantity('25')
        self.itemElementPage.add_element(3)
        number = self.itemElementPage.get_number_of_element()
        self.assertTrue(number == '28')

    #@unittest.skip("Not now") # test falla
    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemPage.select_by_text('Product Name: A to Z')
        self.itemPage.select_by_value('reference:asc')
        self.itemPage.select_by_index(4)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()