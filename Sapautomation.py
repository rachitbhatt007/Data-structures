from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://webdispatcher.dituniversity.edu.in:8169/irj/portal")
user_id= driver.find_element_by_xpath('//*[@id="logonuidfield"]')
user_id.send_keys('1000008746')
password=driver.find_element_by_xpath('//*[@id="logonpassfield"]')
password.send_keys('jamesbond007')
login_button=driver.find_element_by_xpath('//*[@id="UMELogon"]/table[1]/tbody/tr[5]/td[2]/input')
login_button.click()
