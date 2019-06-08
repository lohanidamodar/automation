import sys
import os 
from selenium import webdriver


path = "/home/lohanidamodar/Documents/projects/"
browser = webdriver.Chrome()
browser.get('http://github.com/login')

username = 'lohanidamodar' #your github username
password = '' #your password

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username) 
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0] 
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new') 
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0] 
    python_button.send_keys(folderName)
    python_button = browser.find_elements_by_xpath("//input[@id='repository_visibility_private']")[0]
    python_button.click()
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()
    browser.quit()

if __name__ == "__main__":
    create()