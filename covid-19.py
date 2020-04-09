from plyer import notification
import requests
import sys 
import lxml.html as lh
import pandas as pd
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('umerop.html', 'w') 
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon= '/home/sahil/Desktop/index.jpeg',
        timeout=10
    )

def getData(url):
    r=requests.get(url)
    return r.text

# if _name_ == "_main_":
if __name__=='__main__':

 notifyMe("Umer","lets stop the spread of this virus together")
 myHtmlData = getData('https://www.mohfw.gov.in/')
 # print(myHtmlData)
 # ----------------------#
url='https://www.mohfw.gov.in/'
page = requests.get(url)
doc=lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
# print([len(T) for T in tr_elements[:34]])
# print([T for T in tr_elements[:34]])
#Create empty list
col=[]
i=0#For each row, store each first element (header) and an empty list
# take=int(input())
for take in range(1,32):
    k=0
    for t in tr_elements[take]:
        i+=1
        name=t.text_content()
        print('%d:'%(i),tr_elements[0][k].text_content(),': %s'%(name))
        col.append((name,[]))
        k+=1

#Since out first row is the header,
# data is stored on the second row onwards
for j in range(0,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=33:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1
# print([len(C) for (title,C) in col])

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
# print(df.head())
# print(df)
# for x in range(0,5):
    # for i in df[:x]:
        # print(df[i][x])