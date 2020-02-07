from bs4 import BeautifulSoup
import requests
import json
import re

root_url = "https://theinternship.io/"
resp = requests.get(root_url)
emp=list()
if resp.ok:    
    #data_image = BeautifulSoup(resp.text, features="html.parser").find_all("img")
    #data_text=BeautifulSoup(resp.text, features="html.parser").find_all("span")

    order = dict()

    partners = BeautifulSoup(
                resp.text, features="html.parser").find_all(
                "div", {"class": "partner", "data-v-018ba4ef": ""})
    
    for part in partners:
        order.update({len(part.find("span").getText()): part.find("img").get("src")})

    for i in sorted(order, reverse=True):
        print(order[i])

    """
    div = None
    
    for div in div_data:
        if div.get("data-v-018ba4ef") and div.get("class") == "columns is-multiline":
            break
    """

        
    """
    for i in len(data_image):
        #print(data_text)
        link_image=data_image.get("src")



        link_text=data_text.contents
        if "company/" in link_image[i]:
            #emp.append(link_image[i])
            print(link_image[i])
            print(link_text[i])
    """

