#
import sys
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.support.ui import Select



def timetable(driver,terms,subject):
	
	term = Select(driver.find_element_by_id('_ctl0_MainContent_ddlTerm'))
	term.select_by_value(terms)

	course_type= Select(driver.find_element_by_id('_ctl0_MainContent_ddlSubj_1'))
	course_type.select_by_value(subject) 

	button = driver.find_element_by_name('_ctl0:MainContent:btnSubmit')
	button.click()
	
	table_id = driver.find_element_by_id('_ctl0_MainContent_dgdSearchResult')
	rows = table_id.find_elements_by_tag_name("tr") 
	for row in rows:
		
		colm = row.find_elements_by_tag_name("td")
		for col in colm:
			h=col.text
			print ("{:s}".format(h) , end=' ')
		print()
		print()	
	

def term(driver):
	
	term = Select(driver.find_element_by_id('_ctl0_MainContent_ddlTerm'))
	for option in term.options:
		print (option.text)

def courses(driver):
	
	course_type= Select(driver.find_element_by_id('_ctl0_MainContent_ddlSubj_1'))
	for option in course_type.options:
		print (option.get_attribute('value'),option.text)

def main():
	driver=webdriver.PhantomJS()
	driver.get('http://www2.monmouth.edu/muwebadv/wa3/search/SearchClassesV2.aspx')

	if len(sys.argv) == 2:
		if sys.argv[1] == '--terms':
			term(driver)
		if sys.argv[1] == '--courses':
			courses(driver)
	if len(sys.argv) == 3:
	  timetable(driver,sys.argv[1],sys.argv[2])


if __name__ == '__main__':
  main()
