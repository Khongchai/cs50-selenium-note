from selenium import webdriver
import os
import pathlib
import unittest

PATH = "D:\Edge Webdriver\msedgedriver.exe"
driver = webdriver.Edge(PATH)

def getURI(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()



#find plus and minus button then perform 100 clicks on either 
#try steps below in shell

"""
driver.get(getURI("temp.html"))

increaseButton = driver.find_element_by_id("increase")
increaseButton.click()

decreaseButton = driver.find_element_by_id("decrease")
decreaseButton.click()

for i in range(100):
    increaseButton.click()
"""
class WebpageTests(unittest.TestCase):

    def test_title(self):
        """Check if title is correct """
        driver.get(getURI("temp.html"))
        self.assertEqual(driver.title, "Counter")


    def test_increase(self):
        """Check incrementing a value"""
        driver.get(getURI("temp.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(int(driver.find_element_by_id("number").text), 1)

    
    def test_decrease(self):
        """Check decrementing a value"""
        driver.get(getURI("temp.html"))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(int(driver.find_element_by_id("number").text), -1)

    
    def test_multiple_increase(self):
        """test multiple times"""
        driver.get(getURI("temp.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(int(driver.find_element_by_id("number").text), 3)


#if runs directly from this module, turn on the "test" mode.    
if __name__ == "__main__":
    unittest.main()
    
