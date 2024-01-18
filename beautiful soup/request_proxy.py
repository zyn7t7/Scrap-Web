import requests


# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "https://10.10.1.10:1080",
# }
##  ##  ##  ##  ##  ##  ##  ##
# requests.get("http://example.org", proxies=proxies)
#################################
### TO FIND YOU OWN IP ####
 # THESE PROXIES DID'NT WORK #
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "https://10.10.1.10:1080",
# }

# r = requests.get("https://api64.ipify.org?format=json")
# print(r.json())

####################################
###### CHANGE YOUR IP USING DIFFERENT PROXY ...USING PROXYLAB OR etc ###
proxies = {
  "http": ".............",  #write your own proxy here
  "https": "............",  #write your own proxy here
}

r = requests.get("https://api64.ipify.org?format=json", proxies=proxies)
print(r.json())
#######################################