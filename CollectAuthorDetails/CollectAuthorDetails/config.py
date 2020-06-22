from robot.libraries.BuiltIn import BuiltIn
from robot.libraries import OperatingSystem
from ExcelLibrary import ExcelLibrary
from SeleniumLibrary import SeleniumLibrary
import time ,os, sys

url = "https://www.ncbi.nlm.nih.gov/pmc/"
startdate = '2020-01-15'
enddate = '2020-01-20'
browser = 'chrome'
DELAY = '0.2s'

#Instances creation for Robot Framework Libraries
seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
builtinlib=BuiltIn().get_library_instance('BuiltIn')
excellib=BuiltIn().get_library_instance('ExcelLibrary')

main_path = os.path.abspath(os.curdir)
TestdataFilePath = os.path.join(main_path + "\\testdata.xls")
location = r"C:\Users\abadam\Downloads\pmc_result.xml"

#locators
searcch_text_field_loc = "//input[@class='jig-ncbiclearbutton jig-ncbiautocomplete']"
search_text = "biotechnology"
search_button_loc = "//button[@class='button_search nowrap']"
custom_range_loc = "//li[@class='daterange']/a"
start_year_loc = "//input[@id='facet_date_st_yearpubdate']"
start_month_loc = "//input[@id='facet_date_st_monthpubdate']"
start_day_loc = "//input[@id='facet_date_st_daypubdate']"
end_year_loc = "//input[@id='facet_date_end_yearpubdate']"
end_month_loc = "//input[@id='facet_date_end_monthpubdate']"
end_day_loc = "//input[@id='facet_date_end_daypubdate']"
apply_loc = "//button[@id='facet_date_range_applypubdate']"
links_loc = "//div[@class='rprt']"
page_no = "//input[@id='pageno']"
next_loc = "//div[@class='title_and_pager']//a[@title='Next page of results']"
send_to_loc= "//a[@sourcecontent='send_to_menu']"
file_loc = "//input[@id='dest_File']"
format_loc = "//select[@id='file_format']"
format_dropdown_option = 'XML'
create_file_loc = "//div[@id='submenu_File']//button[text()='Create File']"