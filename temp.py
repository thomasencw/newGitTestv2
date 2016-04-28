# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


my_variable=10

def test1():
    result = my_variable*2
    return result
    
print(test1());


string1 = "vi tester lige " + "den foerste"
print(string1.upper());

indsat1 = "numero uno"
indsat2 = "svarnumero due"
indsat3 = "og nummer hvad?"#for input skriv : input("og nummer hvad")
print("når man siger %s, må man også sige %s.. og så kommer nummer %s" %(indsat1, indsat2, indsat3))

from datetime import datetime
now = datetime.now()
print(now)
current_year = now.year
#gælder også for  day og month