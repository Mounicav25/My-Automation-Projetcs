from config import *
import time,xlwt
import xml.etree.ElementTree as ET
from os import path
from selenium import webdriver

def collect_author_details():

    if (str(path.isfile(location)) == 'True'):
        os.remove(location)
        builtinlib.log("Successfully removed the file")
        return True
    else:
        builtinlib.log("Unable to locate the file")

    seleniumlib.set_selenium_speed(DELAY)

    startdate_slipt = startdate.split("-")
    enddate_slipt = enddate.split("-")
    startyear  = startdate_slipt[0]
    startmonth = startdate_slipt[1]
    startday = startdate_slipt[2]
    endyear = enddate_slipt[0]
    endmonth = enddate_slipt[1]
    endday = enddate_slipt[2]

    #seleniumlib.open_browser(url, browser)
    open_chrome_browser(url)
    seleniumlib.maximize_browser_window()
    seleniumlib.input_text(searcch_text_field_loc, search_text)
    seleniumlib.click_element(search_button_loc)
    time.sleep(3)
    seleniumlib.click_element(custom_range_loc)
    seleniumlib.input_text(start_year_loc, startyear)
    seleniumlib.input_text(start_month_loc, startmonth)
    seleniumlib.input_text(start_day_loc, startday)
    seleniumlib.input_text(end_year_loc, endyear)
    seleniumlib.input_text(end_month_loc, endmonth)
    seleniumlib.input_text(end_day_loc, endday)

    seleniumlib.click_element(apply_loc)
    time.sleep(3)

    links_count = len(seleniumlib.get_webelements(links_loc))
    global total_pages_count
    total_pages_count = 0
    if links_count > 0:
        try:
            total_pages_count = seleniumlib.get_element_attribute(page_no,attribute='last')
        except:
            builtinlib.log("no pagination")
        pages_count = int(total_pages_count)+1
        if total_pages_count > 0:
            for i in range(1, pages_count):
                if i>1:
                    seleniumlib.click_element(next_loc)
                    time.sleep(4)

                links_count = len(seleniumlib.get_webelements(links_loc))

                for j in range(1, links_count+1):
                    seleniumlib.click_element(links_loc + "[" + str(j) + "]//input")

            xml_generation()

        else:
            for j in range(1, links_count+1):
                seleniumlib.click_element(links_loc+"["+str(j)+"]//input")
            xml_generation()
    else:
        builtinlib.log("No data available in the given date range")

def open_chrome_browser(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--safebrowsing-disable-extension-blacklist")
    options.add_argument("--safebrowsing-disable-download-protection")
    prefs = {'safebrowsing.enabled': 'true'}
    options.add_experimental_option("prefs", prefs)
    instance = seleniumlib.create_webdriver('Chrome', desired_capabilities=options.to_capabilities())
    seleniumlib.go_to(url)

def xml_generation():
    seleniumlib.set_selenium_speed(DELAY)
    seleniumlib.click_element(send_to_loc)
    seleniumlib.click_element(file_loc)
    seleniumlib.select_from_list_by_value(format_loc,format_dropdown_option)
    seleniumlib.click_element(create_file_loc)
    time.sleep(60)

    global count
    count = 1

    tree = ET.parse(location)
    root = tree.getroot()
    time.sleep(2)

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('AuthorDetails')
    wb.save('testdata.xls')
    sheet1.write(0, 0, 'Firstname')
    sheet1.write(0, 1, 'Surname')
    sheet1.write(0, 2, 'Email Id')
    wb.save('testdata.xls')

    for mail in root.findall(".//*[@contrib-type='author']"):

        name_tag = 'NA'
        address_tag = 'NA'
        for l in range(0, len(mail.getchildren())):
            if mail.getchildren()[l].tag == 'name':
                name_tag = mail.getchildren()[l]
            elif mail.getchildren()[l].tag == 'address':
                address_tag = mail.getchildren()[l]
        try:
            print("surname - "+name_tag.find('surname').text)
            print("firstname - " + name_tag.find('given-names').text)
            sheet1.write(count, 0, name_tag.find('given-names').text)
            sheet1.write(count, 1, name_tag.find('surname').text)
            try:
                sheet1.write(count, 2, address_tag.find('email').text)
                author_mail = address_tag.find('email').text
                print("mail - " + author_mail)
            except:
                try:
                    mul_email = mail.findall('email')
                    mul_email_collection = mul_email[0].text
                    for k in range(1, len(mul_email)):
                        mul_email_collection = mul_email_collection + "," + mul_email[k].text

                    print("mul_email_collection - " + mul_email_collection)
                    sheet1.write(count, 2, mul_email_collection)

                except:
                    print('email NA')
                    sheet1.write(count, 2, 'NA')
            count = count + 1
            wb.save('testdata.xls')
        except:
            builtinlib.log("No user details")


