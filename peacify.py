# Only works Tenda router!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import socket

def getMyIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0].split('.')[3]
    s.close()
    return ip

driver = webdriver.Chrome('./chromedriver.exe')

# Load a page 
driver.get('http://192.168.0.1/')

inputElement = driver.find_element_by_class_name("input-medium")
inputElement.send_keys('admin')

btnElement = driver.find_element_by_class_name("btn-link")
btnElement.click()

print(driver.current_url)

btnElement = driver.find_element_by_id("submit_ok")
btnElement.click()

bandwidthTab = driver.find_element_by_id("bandwidth")
bandwidthTab.click()

# HTML - Selenium Crap goes here
container = driver.find_element_by_xpath("//*[@id='container_main']")
innerFrame = container.find_element_by_xpath("//*[@id='main_iframe']")
driver.switch_to.frame(innerFrame)

txtStartIP = driver.find_element_by_xpath("//*[@id='bandwith_box']/tbody/tr[1]/td[2]/input[1]")
txtEndIP = driver.find_element_by_xpath("//*[@id='bandwith_box']/tbody/tr[1]/td[2]/input[2]")

bandwidthMin = driver.find_element_by_xpath("//*[@id='bandwith_box']/tbody/tr[3]/td[2]/input[1]")
bandwidthMax = driver.find_element_by_xpath("//*[@id='bandwith_box']/tbody/tr[3]/td[2]/input[2]")

btnAddToList = driver.find_element_by_xpath("//*[@id='add-to-list']/input")
btnConfirmAdd = driver.find_element_by_xpath("/html/body/form/div/input[1]")

selectLinkType = Select( driver.find_element_by_xpath("//*[@id='bandwith_box']/tbody/tr[2]/td[2]/select") )
chkEnable = driver.find_element_by_xpath("//*[@id='bandwith_box']/tbody/tr[4]/td[2]/input")

whiteListIP = int(getMyIPAddress())
if(whiteListIP == 100):
    txtStartIP.send_keys('101')
    txtEndIP.send_keys('110')

    selectLinkType.select_by_index(1)
    chkEnable.click()

    bandwidthMin.send_keys('1')
    bandwidthMax.send_keys('1')
    
    btnAddToList.click()
else:
    startIP = 100
    endIP = whiteListIP - 1

    selectLinkType.select_by_index(1)
    chkEnable.click()

    txtStartIP.send_keys(str(startIP))
    txtEndIP.send_keys(str(endIP))
    bandwidthMin.send_keys('1')
    bandwidthMax.send_keys('1')
    btnAddToList.click()

    startIP = whiteListIP + 1
    endIP = 110

    txtStartIP.clear()
    txtEndIP.clear()
    txtStartIP.send_keys(str(startIP))
    txtEndIP.send_keys(str(endIP))
    btnAddToList.click()

btnConfirmAdd.click()
driver.close()