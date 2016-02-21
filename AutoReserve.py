# Copyright 2015
#
# Author : Tarun Atrey
#
# Python script to do reservation for community Tennis courts.
#

import time
from splinter import Browser
from selenium.webdriver.common.keys import Keys

strUsername = 'XYZ@gmail.com'
strPassword = 'PASSWORD\n'
strDate = '01/01/2016'
strTime = '1:00 PM'
strDuration = '1.5 hours' 


with Browser() as browser:
    browser.visit('https://elan.activebuilding.com')
    time.sleep(2)
    browser.find_by_id('email').fill(strUsername)
    browser.find_by_id('password').fill(strPassword)
    time.sleep(5)
    browser.visit('https://elan.activebuilding.com/portal/reservations/step1/?amenityId=1743')

    #select date for reservation
    browser.find_by_id('startDate').fill(strDate)
    browser.find_by_id('content').click()

    #select time for reservation
    el1 = browser.find_by_id('startTime')
    for option in el1.find_by_tag('option'):
        if option.text == '1:00 PM':
            option.click()
            break

    #select duration for reservation
    el2 = browser.find_by_id('durationHours')
    for option in el2.find_by_tag('option'):
        if option.text == '1.5 hours':
            option.click()
            break

    #submit step1 for the form
    browser.find_by_id('submit-reservation-step1').click()

    #select checkbox to acknowledge rules and regulations
    browser.find_by_id('approve-regulations').click()

    #submit step2 for the form
    browser.find_by_id('submit-reservation-step2').click()

    time.sleep(5)
