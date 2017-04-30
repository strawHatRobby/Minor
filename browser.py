from selenium import webdriver
from pyvirtualdisplay import Display

class Browser(object):

    display = Display(visible=0, size=(800, 600))
    display.start()
    base_url = 'http://0.0.0.0:8080'
    driver = webdriver.Chrome()
    

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)
