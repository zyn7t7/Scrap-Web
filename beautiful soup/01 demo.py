import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())    #return the code in sample.html
# print(soup.title, type(soup.title)) 
# print(soup.title, type(soup.title.string)) 
# print(soup.div) 
# print(soup.find_all("div")) 
# print(soup.find_all("div")[0])      #return first div
#########
# for link in soup.find_all("a"):       #return href in sample.html
#     print(link.get("href"))
#     print(link.get_text())      #return everylink and text

#########
# s = soup.find(id="link3")
# print(s)
# print(s.href)   #return none
# print(s.get("href"))   #returns href
########
# print(soup.select("div.italic"))    #return classes .
# print(soup.select("div#italic"))    #return id .

##### TO FIND CHILDREN IN DIV ###
# for child in soup.find(class_="container").children:
#     print(child)
    
# for parent in soup.find(class_="box").parents:
#     print(parent)

######################
# i = 0
# for parent in soup.find(class_="box").parents:
#     i += 1
#     print(parent)
#     if(i==2):
#         break
##########################
######## TAG CHANGE ###
# cont = soup.find(class_="container")
# cont.name = "span"
# print(cont)
###########
# cont["class"]= "my class"
# print(cont)
###########
# cont.string = "i am a string"
# print(cont)
###############################
ulTag = soup.new_tag["ul"]

liTag = soup.new_tag["li"]
liTag.string = "Home"

liTag = soup.new_tag["li"]
liTag.string = "About"

soup.html.body.insert(0, ulTag)
with open("modified.html","w") as f:
    f.write(str(soup))