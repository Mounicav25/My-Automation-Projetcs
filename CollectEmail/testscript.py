from config import *
import time,xlwt
import os,sys
import subprocess

def open_browser():
    seleniumlib.open_browser(url, 'chrome')
    time.sleep(2)
    seleniumlib.maximize_browser_window()

def Agricultural_Biological_Sciences():
    try:
        seleniumlib.click_element(life_science_sub_links+"[1]")
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('Agricultural',Life_science_TestdataFilePath)
    except:
        seleniumlib.click_element(life_science_link)
        seleniumlib.click_element(life_science_sub_links+"[1]")
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('Agricultural',Life_science_TestdataFilePath)


def collect_email(sheetname1,Path):
    seleniumlib.set_selenium_speed(DELAY)
    global wb
    wb = xlwt.Workbook()

    try:
        journals_pagination_count = seleniumlib.get_text(journals_pagination_loc)
        journals_pagination_count_slipt = journals_pagination_count.split(" ")
        journals_pages_count = journals_pagination_count_slipt[3]
    except:
        journals_pages_count = 1

    journals_url = seleniumlib.get_location()

    #Journals pagination loop
    for jornal in range(0,int(journals_pages_count)):
        builtinlib.log("Journals pagination - "+str(jornal))
        global count
        count = 0
        global sheet1
        sheet1 = wb.add_sheet(str(jornal+1)+"_"+sheetname1+"_"+str(jornal+1))
        sheet1.write(0, 0, 'Publication Title')
        sheet1.write(0, 1, 'Title')
        sheet1.write(0, 2, 'Author Name')
        sheet1.write(0, 3, 'Email ID')
        wb.save(Path)
        if jornal > 0:
            for next_loop in range(0, jornal):
                seleniumlib.click_element(journals_next_button_loc)
                time.sleep(3)

        journals_count = seleniumlib.get_element_count(journals_list)
        builtinlib.log("email count - " + str(journals_count))

        #Journal individual links loop
        for i in range(0, int(journals_count)):
            builtinlib.log("Journals count - " + str(i))
            seleniumlib.click_element(journals_list + "[" + str(i + 1) + "]/a")
            time.sleep(2)
            seleniumlib.click_element(all_issues)
            time.sleep(3)

            try:
                volumes_pagination_count = seleniumlib.get_text(journals_pagination_loc)
                volumes_pagination_count_slipt = volumes_pagination_count.split(" ")
                volumes_pages_count = volumes_pagination_count_slipt[3]
            except:
                volumes_pages_count = 1

            builtinlib.log("Volumes pagination - " + str(volumes_pages_count))

            #volumes pagination loop
            for vol in range(0, int(volumes_pages_count)):
                if vol > 0:
                    seleniumlib.click_element(journals_next_button_loc)
                    time.sleep(2)

                volumes_url = seleniumlib.get_location()
                volumes_expand_count = seleniumlib.get_element_count(volumes_expand_link)
                builtinlib.log("Volumes expand icon count - "+str(volumes_expand_count))

                #volumes expand links loop
                for j in range(0, volumes_expand_count):
                    if j > 0:
                        seleniumlib.click_element(volumes_expand_link + "[1]//*[@class='icon icon-navigate-up accordion-icon navigate-up']")
                        time.sleep(2)
                        seleniumlib.click_element(volumes_expand_link + "[" + str(j + 1) + "]")
                        time.sleep(2)

                    volumes_count = seleniumlib.get_element_count(volumes_link)
                    #voulmes list loop for each volumes expand
                    for k in range(0, volumes_count):
                        seleniumlib.click_element(volumes_link + "[" + str(k + 1) + "]/a")
                        time.sleep(4)
                        articles_url = seleniumlib.get_location()
                        articles_list_count = seleniumlib.get_element_count(articles_list_loc)
                        builtinlib.log("articles count - "+str(articles_list_count))

                        #articles loop
                        for l in range(0, articles_list_count):
                            try:
                                seleniumlib.page_should_contain_element(articles_list_loc+articles_sub_lin_loc)

                                articles_sub_list1_count = seleniumlib.get_element_count(articles_list_loc+articles_sub_lin_loc)
                                builtinlib.log("sub articles1 count - " + str(articles_sub_list1_count))

                                for art1 in range(0,articles_sub_list1_count):

                                    seleniumlib.click_element("("+articles_list_loc+articles_sub_lin_loc+")["+str(art1+1)+"]"+articles_link)
                                    time.sleep(2)
                                    articles_link_count = seleniumlib.get_element_count(author_links_loc)
                                    for m in range(0, articles_link_count):
                                        publication_title = seleniumlib.get_text(publication_title_loc)
                                        volume_detail_text = seleniumlib.get_text(volume_details_loc)
                                        builtinlib.log("publication - "+publication_title+"  volume details - "+str(volume_detail_text))
                                        try:
                                            title = seleniumlib.get_text(title_loc)
                                        except:
                                            title = seleniumlib.get_text(title2_loc)
                                        seleniumlib.click_element(author_links_loc + "[" + str(m + 1) + "]")
                                        time.sleep(2)
                                        try:
                                            firstname = seleniumlib.get_text(author_name_loc)
                                            lastname = seleniumlib.get_text(author_surname_loc)
                                            name = firstname + " " + lastname
                                            seleniumlib.page_should_contain_element(email_loc)
                                            email = seleniumlib.get_text(email_loc)
                                            count = count + 1
                                            sheet1.write(count, 0, publication_title)
                                            sheet1.write(count, 1, title)
                                            sheet1.write(count, 2, name)
                                            sheet1.write(count, 3, email)
                                            wb.save(Path)
                                            time.sleep(1)
                                            seleniumlib.click_element(close_icon_loc)
                                        except:
                                            time.sleep(1)
                                            seleniumlib.double_click_element(close_icon_loc)

                                    seleniumlib.go_to(articles_url)
                                    time.sleep(2)


                            except:
                                seleniumlib.page_should_not_contain_element(articles_list_loc + articles_sub_lin_loc)
                                seleniumlib.click_element(articles_list_loc + "[" + str(l + 1) + "]" + articles_link)
                                time.sleep(2)
                                articles_link_count = seleniumlib.get_element_count(author_links_loc)
                                for m in range(0, articles_link_count):
                                    publication_title = seleniumlib.get_text(publication_title_loc)
                                    volume_detail_text = seleniumlib.get_text(volume_details_loc)
                                    builtinlib.log("publication - " + publication_title + "  volume details - " + str(volume_detail_text))
                                    try:
                                        title = seleniumlib.get_text(title_loc)
                                    except:
                                        title = seleniumlib.get_text(title2_loc)

                                    seleniumlib.click_element(author_links_loc + "[" + str(m + 1) + "]")
                                    time.sleep(2)
                                    try:
                                        firstname = seleniumlib.get_text(author_name_loc)
                                        lastname = seleniumlib.get_text(author_surname_loc)
                                        name = firstname + " " + lastname
                                        seleniumlib.page_should_contain_element(email_loc)
                                        email = seleniumlib.get_text(email_loc)
                                        count = count + 1
                                        sheet1.write(count, 0, publication_title)
                                        sheet1.write(count, 1, title)
                                        sheet1.write(count, 2, name)
                                        sheet1.write(count, 3, email)
                                        wb.save(Path)
                                        seleniumlib.click_element(close_icon_loc)
                                    except:
                                        seleniumlib.click_element(close_icon_loc)

                                seleniumlib.go_to(articles_url)
                                time.sleep(2)

                        seleniumlib.go_to(volumes_url)
                        time.sleep(2)

                        try:
                            if j > 0:
                                seleniumlib.click_element(volumes_expand_link + "[1]//*[@class='icon icon-navigate-up accordion-icon navigate-up']")
                                time.sleep(1)
                                seleniumlib.click_element(volumes_expand_link + "[" + str(j + 1) + "]")
                                time.sleep(1)
                        except:
                            builtinlib.log("articles loop end")

                    seleniumlib.go_to(volumes_url)
                    time.sleep(2)

                seleniumlib.go_to(volumes_url)
                time.sleep(2)

            seleniumlib.close_browser()
            time.sleep(2)
            subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
            subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
            seleniumlib.open_browser(journals_url, 'chrome')
            time.sleep(2)
            seleniumlib.maximize_browser_window()

            if jornal > 0:
                for next_loop in range(0,jornal):
                    seleniumlib.click_element(journals_next_button_loc)
                    time.sleep(1)

        seleniumlib.go_to(journals_url)


def Biochemistry():
    try:
        seleniumlib.click_element(life_science_sub_link2)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('Biochemistry',Life_science_TestdataFilePath2)
    except:
        seleniumlib.click_element(life_science_link)
        seleniumlib.click_element(life_science_sub_link2)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('Biochemistry',Life_science_TestdataFilePath2)


def Environmental_Science():
    try:
        seleniumlib.click_element(life_science_sub_link3)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('ES',Life_science_TestdataFilePath3)
    except:
        seleniumlib.click_element(life_science_link)
        seleniumlib.click_element(life_science_sub_link3)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('ES',Life_science_TestdataFilePath3)


def Immunology_and_Microbiology():
    try:
        seleniumlib.click_element(life_science_sub_link4)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('IM',Life_science_TestdataFilePath4)
    except:
        seleniumlib.click_element(life_science_link)
        seleniumlib.click_element(life_science_sub_link4)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('IM',Life_science_TestdataFilePath4)


def Neuroscience():
    try:
        seleniumlib.click_element(life_science_sub_link5)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('Neuroscience',Life_science_TestdataFilePath5)
    except:
        seleniumlib.click_element(life_science_link)
        seleniumlib.click_element(life_science_sub_link5)
        time.sleep(2)
        seleniumlib.click_element(journals_loc)
        time.sleep(5)

        collect_email('Neuroscience',Life_science_TestdataFilePath5)

