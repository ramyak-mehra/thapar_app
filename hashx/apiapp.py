import requests
import json
import urllib.request
import os

# f = open('file.txt', "w")


def fetch_data(resURL):
    l = []
    url = "https://www.googleapis.com/drive/v3/files?q=%27" + resURL + "%27+in+parents&key=AIzaSyCLsjQI8bnfyuh9-FKy-eH87Uq_wUG0H0Y&fields=*"
    # print(url)
    response = requests.request("GET", url, headers={}, data={})
    json_data = json.loads(response.text.encode('utf8'))
    # f.write(json.dumps(json_data, indent=4, sort_keys=True))
    try:
        for file in json_data["files"]:
            name = file["name"]
            file_id = file["id"]
            l.append(tuple((name, file_id)))
    except:
        print("Didnt work")

    return l


fetch_data("14usany7y80NDQkasoaWix8qCpRVHDjb")
