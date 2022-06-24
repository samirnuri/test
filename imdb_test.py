import requests
import urllib3
import pytest
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import time
 
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    'credentials_enable_service': False,
    'profile': {'password_manager_enabled': False},
    "excludeSwitches": ["enable-automation"],
    'useAutomationExtension': False,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1,
  })

driver = webdriver.Chrome(chrome_options=chrome_options)
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
driver.maximize_window()
driver.get("https://www.imdb.com/")
time.sleep(3)

wait = WebDriverWait(driver, 10)
print('Finding movie by menu...\n*******************************************************************')
driver.find_element(By.XPATH, '//*[@id="imdbHeader-navDrawerOpen--desktop"]').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[3]/span/div/div/ul/a[1]/span').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="right-5-react"]/div/div[2]/div[16]/span[4]/a').click()
time.sleep(4)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'The Jazz Singer')]")))
driver.find_element(By.XPATH, '//*[@id="center-3-react"]/div/div/div[2]/h3/div/div/div/div[2]/div[2]/div[2]/div[1]/span/span/a').click()
time.sleep(4)

file1 = open("stringfile.txt","w")
Director_name_menu = [driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]').text]
Writers_menu = [driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]').text]
Stars_menu = [driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]').text]
file1.writelines(Director_name_menu)
file1.writelines('\n')
file1.writelines(Writers_menu)
file1.writelines('\n')
file1.writelines(Stars_menu)
file1.close()

print('Turn to mainpage...\n*******************************************************************')
driver.find_element(By.XPATH, '//*[@id="home_img_holder"]').click()
time.sleep(4)
print('Finding movie by search tab...\n*******************************************************************')
driver.find_element(By.XPATH, '//*[@id="suggestion-search"]').send_keys('The Jazz Singer')
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a').click()
time.sleep(4)

Director_name_searchtab = [driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]').text]
Writers_searchtab = [driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]').text]
Stars_searchtab = [driver.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]').text]

if Director_name_menu == Director_name_searchtab :
    print ("Director name's is verified and correct!!\n*******************************************************************")
else:
	print("Director name's can't verified!!\n*******************************************************************")

if Writers_menu == Writers_searchtab :
    print ("Writers is verified and correct!!\n*******************************************************************")
else:
	print("Writers can't verified!!\n*******************************************************************")

if Stars_menu == Stars_searchtab :
    print ("Stars is verified and correct!!\n*******************************************************************")
else:
	print("Stars can't verified!!\n*******************************************************************")

time.sleep(5)

print('Select all photos...\n*******************************************************************')
driver.find_element(By.XPATH, '//*[@id="iconContext-chevron-right-inline"]').click()

arr = []
links = driver.find_elements(By.XPATH, "//div[@id = 'media_index_thumbnail_grid']/a")
for link in links:
    # print(link.get_attribute('href'))
    arr.append(link.get_attribute('href'))
time.sleep(3)

i = 0
while i<len(arr):
    
    if (requests.head(arr[i]).status_code == 200):
        print("Valid link")
	i+=1
    else:
        print("Broken link")
i += 1
print('All photos links valid...\n*******************************************************************')
