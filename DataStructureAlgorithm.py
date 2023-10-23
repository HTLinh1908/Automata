import os
from bs4 import BeautifulSoup

cwd = os.getcwd()

with open('D:\\f\\CS\\New\\0313330856gd2q3lxlxr.xml', 'r', errors='ignore') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")


b_SHDon = Bs_data.find_all('SHDon')
print(type(b_SHDon))
a = str(b_SHDon)
a= a.lstrip('[<SHDon>').rstrip('</SHDon>]')

#os.rename("D:\\f\\CS\\New\\0313330856gd2q3lxlxr.xml", 'D:\\f\\CS\\New\\'+a+".xml")