#Copy and paste the folder address of the xml files you want to change the name, then un-capital the 1st letter. It will change the name of the files into the content in SHDon


import os
from bs4 import BeautifulSoup

destination = (str(input("Please enter the desired destination: ")))

XML_files = os.listdir(destination)
for i in XML_files:
        
    if i[-3:]=='xml':

        with open(destination + '\\' + str(i), 'r', errors='ignore') as f:
            data = f.read()
                
            Bs_data = BeautifulSoup(data, "xml")
                
            b_SHDon = Bs_data.find_all('SHDon')

            SHDon = str(b_SHDon)

            SHDon= SHDon.lstrip('[<SHDon>').rstrip('</SHDon>]')

        os.rename(destination + '\\' + str(i), destination + '\\'+ SHDon + ".xml")



