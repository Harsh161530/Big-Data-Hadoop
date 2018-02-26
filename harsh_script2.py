import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
from pyquery import PyQuery
from openpyxl import Workbook
from openpyxl import load_workbook

wb2 = load_workbook('pythonparse.xlsx')
sheet1 = wb2['Sheet1']
rows = 12130
#zip_column = sheet1['A']
#date_column = sheet1['B']
zipc = []
dates = []
index = 2
print "Reading zipcodes and dates.."
for i in range(1,500):
    cell2 = 'B' + str(i+1)
    dates.append(sheet1[cell2].value)
print "Read complete.."

c = 0
temp_zip = []
# sheet1['C1'] = "Mean Temperature"
filename = "temp"+str(index)+".txt"
with open(filename,"w") as f:
	for i in range(len(dates)):
		z = str(75217)
		day = str(dates[i].day)
		month = str(dates[i].month)
		year = str(dates[i].year)
		url = "https://www.wunderground.com/history/airport/KADS/" + year + "/" + month + "/" + day + "/DailyHistory.html?req_city=Dallas&req_state=TX&reqdb.zip=" + z + "&reqdb.magic=1&reqdb.wmo=99999"
		response = urllib2.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html)
		parsed_html = BeautifulSoup(html)
		temp = parsed_html.body.find('span', attrs={'class':'wx-value'}).text.strip()
		f.write(temp)
		f.write("\n")
		# print "Zip: %s | Temp: %s" % (z, temp)
		# cell = 'C' + str(i+2)
		# sheet1[cell] = temp
		if i % 10 == 0:
			print "Written %d records.." % c
			c += 10 

# Save the file
# wb2.save("pythonparse.xlsx")