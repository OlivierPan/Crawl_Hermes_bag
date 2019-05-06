#coding:utf-8
# Ce script est écrit par Pansa, dans le but de crawler le site Hermès et noctifier automatiquement par un mail d'alerte quand un des trois sacs les plus recherchés sont mis en ligne
import requests
import time
import os
import re
import datetime

start = time.time()
now=datetime.datetime.now()

for root, dirs, files in os.walk("/users/pansa/desktop/hermes/"):
    for name in files:
        if name.endswith(".txt") and "hermes_sac" in name:
            previousFileName=str(os.path.join(root,name))            
print(previousFileName)


list1=[]
with open(previousFileName,"r") as file:
    contents=file.readlines()
    for line in contents:
        if line != "\n":
            list1.append(line)


r=requests.get("https://www.hermes.com/fr/fr/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/#fh_view_size=36&country=fr&fh_location=--%2Fcategories%3C%7Bwomenbagsbagsclutches%7D&fh_start_index=72|relevance|Ligne")


newfilename="/users/pansa/desktop/hermes/hermes_sac_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+".txt"
with open(newfilename,"w") as file:
    file.write(r.text)


end1 = time.time()
print("request and create file time",end1 - start)


list2=[]
with open(newfilename,"r") as file:
    contents=file.readlines()
    for line in contents:
        if line != "\n":
            list2.append(line)



print(len(list1),len(list2))
pattern=re.compile(r"[Pp]icotin|[Ll]indy|[Gg]arden [Pp]arty")
i=1
while i < len(list2):
    if list2[i] not in list1:
            print("-----------------------Differ-------------------at------"+str(i)+"---------")
            if re.findall(pattern,list2[i]):
                print("yes")
                print(re.findall(pattern,list2[i]))
                #send message; à développer
    i+=1
    
os.remove(previousFileName)
         
end2 = time.time()
print("open file and compare difference time",end2 - start)
    
