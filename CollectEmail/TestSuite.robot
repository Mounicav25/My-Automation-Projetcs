*** Settings ***

#External Libraries
Library  SeleniumLibrary
Library  ExcelLibrary
Library  BuiltIn

#User defined Library
Library  testscript.py

Suite Setup  testscript.open_browser
#Test Teardown  Close Browser

*** Test Cases ***
Agricultural_Biological_Sciences
    Agricultural_Biological_Sciences
Biochemistry
    Biochemistry
Environmental_Science
    Environmental_Science
Immunology_and_Microbiology
    Immunology_and_Microbiology
Neuroscience
    Neuroscience

