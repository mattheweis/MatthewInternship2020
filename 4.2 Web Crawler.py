from bs4 import BeautifulSoup
import requests
import json

root_url = "https://theinternship.io/"

resp = requests.get(root_url)
if resp.ok:
    data = BeautifulSoup(resp.text, features="html.parser").find_all("img")
    output = {"companies": [
                    {"logo": root_url + x.get("src")} 
                        for x in data if "company" in x.get("src")]}

with open("output.json", "w+") as f:
    f.write(json.dumps(output))
