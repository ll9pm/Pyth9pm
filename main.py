import json
import requests
import time,base64
from random import  randint
def send_request():
     username = 'F8dXLU1ddOL3sEhG'
     password = '27LXY4hxTVky9g2P'
     host = 'geo.floppydata.com'
     port = '10080'

     proxy = f'http://{username}:{password}@{host}:{port}'

     token = "sk_EdTXz7dTcoIFO5EZSN1IO9RZlp8vu1n50Cq0n0ub6DWgM5jbNIZeoGjR57rZpGHt"
     host = "api.scrapeless.com"
     url="https://ahbhappinessishealth.blogspot.com/2025/11/blog-post.html?m=1"
    # url="https://viikqoye.com/dc/?blockID=402513"
     payload = {
    "actor": "unlocker.webunlocker",
    "proxy": {
        "country": "US",

    },
    "input": {
        "url": url,
        "redirect": True,
        "jsRender": {
            "enabled": True,
            "waitUntil":"domcontentloaded",
            "instructions": [


       {"click": [ "#clickab", 11000]},
         {"wait":randint(15000,30000)},

        ],
       "response": {
                "type": "png",  # png or jpeg
            }
        },
    }

}
     response = requests.post(
        "https://api.scrapeless.com/api/v2/unlocker/request",
        json=payload,
       # proxies={"http": proxy, "https": proxy},

        headers={
            "x-api-token": token,
            "Content-Type": "application/json"
        },
        timeout=60
    )
     print(response.text[0:200])
     imag=response.json()["data"]
     #image_data=base64.b64decode(imag)
     #with open(f'output_image{randint(10000,9999999)}2.png','wb') as f:
       # f.write(image_data)
if __name__ == "__main__":
    for i in range(1000):
      print(i)
      try:
        send_request()
      except Exception as e:
        print(e)
