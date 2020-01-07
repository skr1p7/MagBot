from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import feedparser

def fedora():
	data = feedparser.parse('https://fedoramagazine.org/feed/')
	global link 
	link = data['entries'][0]['link']
	global title
	title = data['entries'][0]['title']
	time.sleep(1)
def main():
	driver = webdriver.Firefox()
	driver.get("https://twitter.com/login")
	username = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
	uName = str(input("Enter the username> "))
	username.send_keys("{}".format(uName))
	time.sleep(2)
	password= driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
	pWord = str(input("Enter the password> "))
	password.send_keys("{}".format(pWord))
	time.sleep(2)
	submit = driver.find_element_by_xpath("//button[text()='Log in']")
	submit.click()

	driver.get("https://twitter.com/compose/tweet")
	textArea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')))
	tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
	time.sleep(10)
	textArea.send_keys(str(title) + " " + str(link))  
	time.sleep(2)
	tweet.click()
fedora()
main()
