from bs4 import BeautifulSoup
import requests
import re
"""
MCU Historical Stock line
from 1997-season4
To 2020 season2

"""
# 用requests库代替urllib.request
#Beautiful库解析网页结构


"""
1997-s4
"""

#伪装浏览器
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


url = 'http://quotes.money.163.com/trade/lsjysj_600115.html?year=1997&season=4'
#url = 'http://quotes.money.163.com/trade/lsjysj_600115.html?year=2020&season=4'
data = []

# line = 55
# row =11

with requests.Session() as response:
    r = response.get(url,headers=headers)
    html = r.content.decode()
    sp = BeautifulSoup(html,'html.parser')
    #remove <th> mar,starting from the first <tr>
    # beautifulSoup returns list object
    trlist = sp.find("table",{"class":"table_bg001 border_box limit_sale"}).findAll("tr")
    table_cells = 0
    # get the cells
    for tr in trlist:
        table_cells += 1
    table_cells -= 1
    
    tdlist = sp.find("table",{"class":"table_bg001 border_box limit_sale"}).findAll("td")
    #print(tdlist)
    #列数(y) * 行数(x) + z
    for x in range(table_cells):
        fields = {}
        fields['HDate'] = tdlist[11*x+0].get_text()
        fields['Open'] = float(tdlist[11*x+1].get_text())
        fields['High'] = float(tdlist[11*x+2].get_text()) 
        fields['Low'] = float(tdlist[11*x+3].get_text())
        fields['Close'] = float(tdlist[11*x+4].get_text())
        fields['Change'] = tdlist[11*x+5].get_text()
        fields['Chg(%)'] = tdlist[11*x+6].get_text()
        #remove the comma in the string,and convert the string to int
        fields['Volume'] = int(tdlist[11*x+7].get_text().replace(',',''))
        fields['Turnover'] = int(tdlist[11*x+8].get_text().replace(',',''))
        fields['Amplitude(%)'] = tdlist[11*x+9].get_text()
        fields['TurnoverRate(%)'] = tdlist[11*x+10].get_text()
        data.append(fields)
     #reverse the list in ASC order   
    data.reverse()
    print(data)

    


   
        
    # data structure ； [{'date':'1997-1-1','open'：'13’},{'date':'1997-1-2','open':'12'}]
    # file type : csv
    #importance : the data is in DESC order. The frist line is in the data of the December
    #and the last line is the data of the January

    
    #some data are null and the blanks are filled with "--" ,we have to notice that 
    # some data like "Volume" could be negative like -0.35,we can't convert this kind of dada to int
    #add all the data to a list

   



    
        


        
        
    
