from pip._vendor import requests
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://stage.mckinsey.edx.org/')
loginbox = driver.find_element_by_xpath('//*[@id="login_id"]')

# Type username
loginbox.send_keys('growth_user7')

loginbutton = driver.find_element_by_xpath('//*[@id="login"]')
loginbutton.click()

time.sleep(15)

# Type password
passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
passwordbox.send_keys('ARbi12.,')

loginbutton.click()

time.sleep(5)

# Click on first course
cardclick = driver.find_element_by_xpath('//*[@id="course-navigation"]/div')
cardclick.click()

time.sleep(10)

# Click on the first lesson
lessonclick = driver.find_element_by_css_selector('.contentCard ul li.courseRow')
lessonclick.click()

time.sleep(10)

# get all links in a page.
links = driver.find_elements_by_tag_name("a")

for link in links:

   print(link.get_attribute('href'))

time.sleep(20)

# Click on next module.

navigationnext = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext.click()

# Attempt assessment

time.sleep(10)

clickonmrqbox = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/div/fieldset/div/div[4]/label/span[1]')
clickonmrqbox.click()

time.sleep(5)

clickonsubmit = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[5]/input[1]')
clickonsubmit.click()

time.sleep(5)

clickonnextquestion = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[5]/input[2]')
clickonnextquestion.click()

time.sleep(5)

clickonmcqbox = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div/fieldset/div/div[2]/label/span[1]/input')
clickonmcqbox.click()

time.sleep(5)

clickonsubmit.click()

time.sleep(5)

clickonnextquestion.click()

time.sleep(5)

clickonmcqbox2 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[3]/div/div/fieldset/div/div[1]/label/span[1]/input')
clickonmcqbox2.click()

time.sleep(5)

clickonsubmit.click()

time.sleep(5)

clickonnextquestion.click()

time.sleep(5)

clickonmcqbox3 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div/div/fieldset/div/div[1]/label/span[1]/input')
clickonmcqbox3.click()

time.sleep(5)

clickonsubmit.click()

time.sleep(5)

clickonreviewgrade = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[5]/input[3]')
clickonreviewgrade.click()

time.sleep(10)

navigationnext2 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext2.click()

time.sleep(10)

pollsradiobutton = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/form/fieldset/div/div[2]/div[1]/input')
pollsradiobutton.click()

time.sleep(5)

pollssubmit = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/form/input')
pollssubmit.click()

time.sleep(5)

navigationnext3 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext3.click()

time.sleep(5)

surveyradioclick1 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/form/table/tbody/tr[1]/td[1]/label/input')
surveyradioclick1.click()

surveyradioclick2 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/form/table/tbody/tr[2]/td[1]/label/input')
surveyradioclick2.click()

surveyradioclick3 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/form/table/tbody/tr[3]/td[1]/label/input')
surveyradioclick3.click()

surveysubmit = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/form/input')
surveysubmit.click()

time.sleep(5)

navigationnext4 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext4.click()

time.sleep(10)

navigationnext5 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext5.click()

time.sleep(10)

imageexplorerbutton = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[1]/button')
imageexplorerbutton.click()

time.sleep(5)

imageexplorerclose = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/button')
imageexplorerclose.click()

time.sleep(5)

navigationnext6 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext6.click()

time.sleep(10)

text_area = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/label/textarea')
text_area.send_keys("Dummy text")

ftesubmitbutton = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[3]/input')
ftesubmitbutton.click()

time.sleep(5)

navigationnext7 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext7.click()

time.sleep(5)

navigationnext8 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext8.click()

time.sleep(10)

mcqnormalselect = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[3]/div[1]/fieldset/div/div[3]/label/span[1]/input')
mcqnormalselect.click()

time.sleep(5)

mcqsubmit = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[3]/div[3]/input')
mcqsubmit.click()

time.sleep(5)

navigationnext9 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext9.click()

time.sleep(10)

mrqnormalselect = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/fieldset/div/div[4]/label/span[1]/input')
mrqnormalselect.click()

time.sleep(5)

mrqsubmit = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[3]/input')
mrqsubmit.click()

time.sleep(5)

navigationnext10 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext10.click()

time.sleep(20)

navigationnext11 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext11.click()

time.sleep(30)

navigationnext12 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext12.click()

time.sleep(10)

navigationnext13 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext13.click()

time.sleep(15)

clickonmessageonchat = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]')
clickonmessageonchat.click()

time.sleep(5)

navigationnext14 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext14.click()

time.sleep(15)

adventuremcqclick = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[1]/div/div/div/div[4]/div/fieldset/div/div[3]/div[2]/input')
adventuremcqclick.click()

time.sleep(2)

adventureletsseebutton = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/div[1]/button[2]')
adventureletsseebutton.click()

time.sleep(2)

navigationnext15 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext15.click()

time.sleep(10)

eocpdf = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[5]/p/a')
eocpdf.click()

time.sleep(5)

win = driver.window_handles
driver.switch_to_window(win[1])
driver.close()
driver.switch_to_window(win[0])

time.sleep(5)

eoctakeaways = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[6]/p/a')
eoctakeaways.click()

time.sleep(5)

win = driver.window_handles
driver.switch_to_window(win[1])
driver.close()
driver.switch_to_window(win[0])

navigationnext16 = driver.find_element_by_xpath('//*[@id="course-lessons"]/div/div/div/div/div/div[5]/div/a[2]')
navigationnext16.click()

time.sleep(10)

testdfb = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/form/div/div[2]/section[1]/div/div[2]/label[1]')
testdfb.click()

testdfbnext = driver.find_element_by_xpath('//*[@id="steps-uid-0"]/div[3]/ul/li[2]/a')
testdfbnext.click()

clickonoverview = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/ul/li[1]/a')
clickonoverview.click()











