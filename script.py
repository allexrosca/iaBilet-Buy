from selenium import webdriver
from time import sleep
import os

alarmFile = "alarm.mp3"
urlSite = 'https://www.iabilet.ro/auth/'
urlConcert = 'https://www.iabilet.ro/bilete-slipknot-metalhead-meeting-2020-49973/?utm_source=HpTopWeb'
nr_bilete = 2


driver = webdriver.Chrome()
driver.get(urlSite)

driver.find_element_by_id("LoginForm_username_or_email").send_keys('email')
driver.find_element_by_id("LoginForm_password").send_keys('password')

driver.find_element_by_name("login").click()

driver.get(urlConcert)

first_categ = []

try:
    first_categ = driver.find_elements_by_class_name('ticket-categ')[1]
except:
    while 1:
        sleep(5)
        try:
            first_categ = driver.find_elements_by_class_name('ticket-categ')[1]
            os.system(alarmFile)
            sleep(5)
            break
        except:
            driver.refresh()

first_categ = first_categ.find_element_by_xpath('//input')
first_categ.find_element_by_xpath('//*[@class="ticket-nr"]').clear()
first_categ.find_element_by_xpath('//*[@class="ticket-nr"]').send_keys(int(nr_bilete))
driver.find_element_by_name('makeBooking').click()

driver.find_element_by_xpath("//*[contains(text(), 'Continuă')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Alege')]").click()
driver.find_elements_by_id('privacy_policy')[1].click()
driver.find_element_by_name('set_address').find_element_by_xpath("//*[@value='Continuă']").click()
# TODO: check all checkboxes

# driver.find_element_by_class_name('payment-method payment-method-libra').find_element_by_xpath('//*[@type="button"').click()
