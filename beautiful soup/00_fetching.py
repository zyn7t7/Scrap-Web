import requests

########################
# r = requests.get(url)
# print(r.text)

##########################
def FetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path, "w")as f:
        f.write(r.text)
        
url = "https://www.amazon.com/"

FetchAndSaveToFile(url ,"data/times.html")
##################################
