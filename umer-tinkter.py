from plyer import notification
import requests
from bs4 import BeautifulSoup
from tkinter import *
import time

def getData(url):
    r = requests.get(url)
    return r.text
def getData2(url):
    r=requests.get(url)
    return r.text

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='C://Users//umer//PycharmProjects//corona//icon1.ico',
        timeout=10
    )
def get_corona_detail():
    url="https://www.mohfw.gov.in/"
    html_data=getData2(url)
    soup=BeautifulSoup(html_data,'html.parser')
    active_status=soup.find("div",class_="status-update").find("h2").get_text()
    a1=active_status
    info_div=soup.find("div",class_="site-stats-count").find_all("li",class_="bg-blue")
    info_div2=soup.find("div", class_="site-stats-count").find_all("li", class_="bg-green")
    info_div3= soup.find("div", class_="site-stats-count").find_all("li", class_="bg-red")
    info_div4 = soup.find("div", class_="site-stats-count").find_all("li", class_="bg-orange")
    all_details = ""
    for item in info_div:
        text = item.find("span").get_text()
        count = item.find("strong").get_text()
        #print(text + ":" + count)
    for item in info_div2:
        text2 = item.find("span").get_text()
        count2 = item.find("strong").get_text()
        #print(text2 + ":" + count2)
    for item in info_div3:
        text3 = item.find("span").get_text()
        count3 = item.find("strong").get_text()
        #print(text3 + ":" + count3)
    for item in info_div4:
        text4 = item.find("span").get_text()
        count4 = item.find("strong").get_text()
        #print(text4 + ":" + count4)
        all_details=all_details + a1+"\n" +text + ":" + count+"\n"+text2 + ":" + count2+"\n"+text3 + ":" + count3+"\n" +text4 + ":" + count4+"\n"

    return( all_details)
def refresh():
   print("Refreshing.....")

root = Tk()
root.geometry("800x450")

root.title("Apna time aayega")
root.configure(background='white')
f = ("poppins", 20, "bold")
# mainLabel2=Label(root,text=a1)
banner = PhotoImage(file="covid1.png")
bannerLabel = Label(root, image=banner)
bannerLabel.pack()
mainLabel = Label(root, text=get_corona_detail(), font=f, bg='red').pack()

button = Button(root, text="REFRESH", font=f, relief='solid', command=refresh).pack()
root.mainloop()




if _name_ == "_main_":
    #print(get_corona_detail())
    myHtmlData = getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    myDatastr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDatastr = tr.get_text()
        myDatastr = myDatastr[1:]
        itemlist = (myDatastr.split("\n\n"))
        states = ['Chandigarh', 'Delhi', 'Goa', 'Manipur']
        for item in itemlist:
             datalist = item.split('\n')
             if datalist[1] in states:
              print(datalist)
              ntitle = 'Cases in Covid-19'
              ntext = f"STATE {datalist[1]}\nTotal:{datalist[2]}\nCured:{datalist[3]}\nDeath:{datalist[4]}"
              notifyMe(ntitle, ntext)