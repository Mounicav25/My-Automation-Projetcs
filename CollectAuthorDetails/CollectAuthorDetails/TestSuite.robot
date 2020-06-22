*** Settings ***

#External Libraries
Library  SeleniumLibrary
Library  ExcelLibrary
Library  BuiltIn

#User defined Library
Library  testscript.py

Test Teardown  Close Browser

*** Test Cases ***
Collect_Author_Details
    collect_author_details