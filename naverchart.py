import options as options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from bs4 import BeautifulSoup

def copy_input(xpath,input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


'''
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
'''
id='dhtngus4921'
pw='xn9jujqC!'
number='01049211573'
driver=webdriver.Chrome('C:/Users/dhtng/Desktop/chromedriver')
driver.implicitly_wait(3)
driver.get('http://nid.naver.com/nidlogin.login')

copy_input('//*[@id="id"]',id)
time.sleep(2)
copy_input('//*[@id="pw"]',pw)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(2)
'''
driver.find_element_by_name('id').send_keys('dhtngus4921')
driver.find_element_by_name('pw').send_keys('xn9jujqC!')
'''
copy_input('//*[@id="phone_area"]',number)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]').click()

driver.get('http://mail.naver.com')
driver.implicitly_wait(3)

def get_mail_list(page_source):
    soup=BeautifulSoup(page_source,"html.parser")
    div_list=soup.select("ol.mailList>li>div.mTitle")
    for div in div_list:
        soup=BeautifulSoup(str(div),"html.parser")
        title=soup.select_one("div.name>a").text
        subject=soup.select_one("div.subject>a:nth-of-type(1)>span>strong").text
        print("{} / {}".format(title,subject))
get_mail_list(driver.page_source)