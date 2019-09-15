from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
# https://selenium-python.readthedocs.io/locating-elements.html

stadiumCourtDict = {
    'BBcourt1': 'Basketball 60 Mins- Crt 1',
    'BBcourt2': 'Basketball 60 Mins- Crt 2'
}

timeslotDict = {
    '6am': 'ctl00$MainContent$grdResourceView$ctl08$ctl00',
    '7am': 'ctl00$MainContent$grdResourceView$ctl09$ctl00',
    '8am': 'ctl00$MainContent$grdResourceView$ctl10$ctl00',
    '9am': 'ctl00$MainContent$grdResourceView$ctl11$ctl00',
    '10am': 'ctl00$MainContent$grdResourceView$ctl12$ctl00',
    '11am': 'ctl00$MainContent$grdResourceView$ctl13$ctl00',
    '12pm': 'ctl00$MainContent$grdResourceView$ctl14$ctl00',
    '1pm': 'ctl00$MainContent$grdResourceView$ctl15$ctl00',
    '2pm': 'ctl00$MainContent$grdResourceView$ctl16$ctl00',
    '3pm': 'ctl00$MainContent$grdResourceView$ctl17$ctl00',
    '4pm': 'ctl00$MainContent$grdResourceView$ctl18$ctl00',
    '5pm': 'ctl00$MainContent$grdResourceView$ctl19$ctl00',
    '6pm': 'ctl00$MainContent$grdResourceView$ctl20$ctl00',
    '7pm': 'ctl00$MainContent$grdResourceView$ctl21$ctl00',
    '8pm': 'ctl00$MainContent$grdResourceView$ctl21$ctl00',
    '9pm': 'ctl00$MainContent$grdResourceView$ctl23$ctl00',
}

confirmButtonDict = {
    'BBcourt1': 'ctl00_MainContent_btnBasket',
    'BBcourt2': 'ctl00_MainContent_btnBasket'
}


opts = Options()
opts.headless = True
# download latest chrome driver from https://sites.google.com/a/chromium.org/chromedriver/home
# make sure support version is correct, e.g 78
# And set PATH=path/to/driver in bash_profile or bashrc
driver = webdriver.Chrome('/Users/joej/Downloads/chromedriver', options=opts)
driver.get('http://fdlcbookings.canadabay.nsw.gov.au/Connect/MRMLogin.aspx')

fdlcUsername = '1060100'
fdlcPassword = '1452'
bookingDate = '19/09/2019'
stadiumCourt = 'BBcourt2'
timeslot = '7pm'


# input type: text
username_field = driver.find_element_by_id('ctl00_MainContent_InputLogin')
username_field.send_keys(fdlcUsername)
# input type: password
password_field = driver.find_element_by_id('ctl00_MainContent_InputPassword')
password_field.send_keys(fdlcPassword)
# input type: submit
submit_button = driver.find_element_by_id('ctl00_MainContent_btnLogin')
submit_button.click()

# input type: date
date_field = driver.find_element_by_id('ctl00_MainContent__advanceSearchUserControl_specificDate')
date_field.send_keys(bookingDate)

# a href onlick
search_button = driver.find_element_by_link_text('Search')
search_button.click()

# to wait for loading results
sleep(3)

# a href onlick
court2 = driver.find_element_by_link_text(stadiumCourtDict[stadiumCourt]) 
court2.click()

# to wait for loading results
sleep(5)

# input type: submit - 21 is 7pm-8pm
slot = driver.find_element_by_name(timeslotDict[timeslot])
slot.click()

# input type: button
book_btn = driver.find_element_by_id(confirmButtonDict[stadiumCourt])
book_btn.click()

print("Booking successful {kind} at {time} on {date}".format(kind=stadiumCourt, time=timeslot, date=bookingDate))
#results = driver.find_elements_by_class_name('result')
#print(results[0].text)




