from robot.libraries.BuiltIn import BuiltIn
from robot.libraries import OperatingSystem
from ExcelLibrary import ExcelLibrary
from SeleniumLibrary import SeleniumLibrary
import time ,os, sys

url = "https://www.sciencedirect.com/#life-sciences"
DELAY = '0.2s'

#Instances creation for Robot Framework Libraries
seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
builtinlib=BuiltIn().get_library_instance('BuiltIn')
excellib=BuiltIn().get_library_instance('ExcelLibrary')

main_path = os.path.abspath(os.curdir)
Life_science_TestdataFilePath = os.path.join(main_path + "\\Life_science_output\\Agricultural_Biological_Sciences.xls")
Life_science_TestdataFilePath2 = os.path.join(main_path + "\\Life_science_output\\Biochemistry_genetics_molecularbiology.xls")
Life_science_TestdataFilePath3 = os.path.join(main_path + "\\Life_science_output\\Environmental_Sciences.xls")
Life_science_TestdataFilePath4 = os.path.join(main_path + "\\Life_science_output\\Immunology_microbiology.xls")
Life_science_TestdataFilePath5 = os.path.join(main_path + "\\Life_science_output\\NeuroSciences.xls")

#Life sciences
life_science_sub_links = "//div[@id='life-sciences']//ul[@class='u-padding-s-ver-from-md no-bullet-points']/li"
life_science_sub_link2 = "(//div[@id='life-sciences']//ul[@class='u-padding-s-ver-from-md no-bullet-points']/li)[2]"
life_science_sub_link3 = "(//div[@id='life-sciences']//ul[@class='u-padding-s-ver-from-md no-bullet-points']/li)[3]//a"
life_science_sub_link4 = "(//div[@id='life-sciences']//ul[@class='u-padding-s-ver-from-md no-bullet-points']/li)[4]//a"
life_science_sub_link5 = "(//div[@id='life-sciences']//ul[@class='u-padding-s-ver-from-md no-bullet-points']/li)[5]//a"
life_science_link = "//a[@href='#life-sciences']"
Healthscience_link = "//a[@href='#health-sciences']"
Physical_science_link = "//a[@href='#physical-sciences-and-engineering']"
Socialhumanity_link = "//a[@href='#social-sciences-and-humanities']"
journals_pagination_loc = "//span[@class='pagination-pages-label']"
journals_loc = "//span[text()='Journals']/parent::label/span[1]"
journals_next_button_loc = "//*[@class='icon icon-navigate-right']"
journals_list = "//li[@class='publication branded u-padding-xs-ver js-publication']"
all_issues = "//span[text()='All issues']"
volumes_expand_link = "//li[@class='accordion-panel js-accordion-panel']"
volumes_link = "//section[@class='js-issue-list-content']/div"
articles_list_loc = "//ol[contains(@class,'article-list-items')]/li"
articles_link = "//a[@class='anchor article-content-title u-margin-xs-top u-margin-s-bottom']"
articles_sub_lin_loc = "//ol[@class='article-list']//li"
articles_subline1_loc = "//ol[@class='article-list']//li[@class='js-jl-aip-group article-item article-item-vertical-line']"
#author_links_loc = "//div[@class='author-group']//a"
author_links_loc="(//*[local-name() = 'svg'][@class='icon icon-envelope'])"
email_loc = "//div[@class='e-address']//a"
publication_title_loc = "//a[@class='publication-title-link']"
title_loc = "//span[@class='title-text']"
title2_loc = "//div[@class='other-ref']/span"
close_icon_loc = "//button[@title='Close']"
author_name_loc = "//div[@class='author']/span[@class='text given-name']"
author_surname_loc = "//div[@class='author']/span[@class='text surname']"
volume_details_loc = "//a[@title='Go to table of contents for this volume/issue']"