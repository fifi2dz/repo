# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Vietnamese Department" : "De Anza College :: Vietnamese :: Home", 
            "Virtual Tour" : "De Anza College :: Virtual Tour :: Home",
            "Visual & Performing Arts Center Rental" : "De Anza College :: Rent the Visual & Performing Arts Center :: Home",
            "Web Publishing Guide" : "De Anza College :: Web Publishing Guide :: Home",
            "Wireless Hot Spot Internet Access" : "De Anza College :: Campus Virtual Tour :: Wireless Access",
            "Women's Studies Department" : "De Anza College :: Women's Studies :: Home",
            "Workforce Education" : "De Anza College :: Workforce Education :: Home",
            "Writing and Reading Center" : "De Anza College :: Writing and Reading Center :: Home",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
         
