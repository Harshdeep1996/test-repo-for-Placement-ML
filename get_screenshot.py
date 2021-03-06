import validators
from selenium import webdriver
from pyvirtualdisplay import Display
from fogbugz import FogBugz

fb = FogBugz("https://cloudant.fogbugz.com")
fb.logon("harshdeep.harshdeep@uk.ibm.com","Harsh1996")

def main(source,times=None):
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Firefox() #Using chrome web driver
	if not validators.url(source): 
		driver.get('file://' + source)
	else:
		driver.get(source) #Fill in URL
	how_many_screenshots(driver,times)
	driver.quit()
	display.stop()

def how_many_screenshots(driver,times):
	elementHeight = driver.find_element_by_tag_name("body").size['height'] 
	if times is None:
		driver.save_screenshot('screenshot_full.png')
		file = open('screenshot_full.png', 'r')
		fb.edit(ixBug=73752, Files={'screenshot_full.png': file})
	else:
		portions = 0
		temp = elementHeight / times
		while(portions < elementHeight):
			driver.execute_script("window.scrollBy(0, %d);" % portions)
			driver.save_screenshot('screenshot_full_%d.png' % portions)
			file = open('screenshot_full_%d.png' % portions, 'r')
			fb.edit(ixBug=73752, Files={'screenshot_full_%d.png' % portions: file})
			portions += temp

if __name__ == '__main__':
    main('https://www.google.com',times=None)