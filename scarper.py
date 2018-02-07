import requests
import re
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

#Intializing Empty variables
studentdata=studentdatasaved=""

#Add you URL here inside make_soup
soup = make_soup("")

for record in soup.findAll('tr'):
    studentdata=""
    for data in record.findAll('td'):
        studentdata=studentdata+","+data.text
    if len(studentdata)!=0:
        #Below line is to remove any whitespace, line breaks and unwanted data.
        studentdata=re.sub(r"[\n\t\s]*", "",studentdata)
        studentdatasaved = studentdatasaved + "\n" + studentdata[1:]

#To store data in .csv in your PC. Change the name according to your need.
file=open(os.path.expanduser("Student.csv"),"wb")
file.write(bytes(header, encoding="ascii",errors="ignore"))
file.write(bytes(studentdatasaved, encoding="ascii",errors="ignore"))
