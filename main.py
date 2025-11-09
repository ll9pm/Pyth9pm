
# Install the Python Requests library:
# `pip install requests`
import requests
import threading
import time,base64
from random import  randint
# Define the number of requests you want to send concurrently
NUM_REQUESTS = 1

def send_request(request_number,api):
    """
    Sends a single HTTP GET request and prints the status and content.
    The 'request_number' is used for clearer identification in the output.
    """
    start_time = time.time()
    thread_name = threading.current_thread().name
    print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Starting Request #{request_number}...")

    try:

        token = api
        username = '05E69D501DC4-proxy-country_US-r_0m-s_zafNekMpy6'
        password = 'A69jWamH'
        host = 'gw-us.scrapeless.io'
        port = '8789'

        proxy = f'http://{username}:{password}@{host}:{port}'
        url="https://viikqoye.com/dc/?blockID=402513"
        url="https://ahbhappinessishealth.blogspot.com/2025/10/blog-post.html"
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


      # {"click": [ "#clickab", 11000]},
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
      headers={
         "x-api-token": token,
         "Content-Type": "application/json"
     },
     timeout=60
 )
        duration = time.time() - start_time
       # print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Finished Request #{request_number}. Status Code: {response.status_code} in {duration:.2f}s")
       # print('Response Body: ',"aliexpress" in response.text) # Uncomment to see the content
        print(response.text[0:200])
        """ imag=response.json()["data"]
        image_data=base64.b64decode(imag)
        with open(f'output_image{randint(10000,9999999)}2.png','wb') as f:
         f.write(image_data)
    """
    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Error in Request #{request_number}: {e}")

def send_requests_with_threading(api):
    """
    Creates and starts 5 threads, each running the send_request function,
    and waits for them all to complete.
    """
    threads = []

    global_start_time = time.time()
    print(f"--- Starting {NUM_REQUESTS} concurrent requests using threads ---")

    # 1. Create and Start Threads
    for i in range(1, NUM_REQUESTS + 1):
        # Create a new Thread object, targeting the send_request function
        thread = threading.Thread(target=send_request, args=(i,api), name=f"WorkerThread-{i}")
        threads.append(thread)
        thread.start() # Immediately start the thread, running the request concurrently

    # 2. Wait for all Threads to Finish (Joining)
    # The main program thread blocks (pauses) at .join() until the corresponding thread finishes.
    for thread in threads:
        thread.join()

    global_duration = time.time() - global_start_time
    print("\n--- All concurrent requests completed ---")
    print(f"Total elapsed time: {global_duration:.2f} seconds")

if __name__ == '__main__':
    for i in range(1000):
      apis =[

          "sk_E3FPwMRuFHFGuGl4JUcW7KCYLvBV1NSXUApSdU05T3QTrswbJNc5OwE7QWWMVOsS",

"sk_JgkeYoCQkZC0LlGUP5NU3hlFLCSoYeCC2KcIl8Hi96f9tkExkO5T9CCi9rMZ3obE",

"sk_GgGut1KEEzInrKHhA9KsZJspR2hD0Cn2zzki4yaHJQ5REzGVUm2MnVRtprBqheiT",

"sk_O0sZWt1pBVy1F5Fq1Qw7wuDbqYFSC6I1r9nzx7WsBeixoEOUUkzIOz1ehDyltqMl",

"sk_hfb6QenUmcCOAHgZCiXYT1JVt10Mi1L2eIISSAccD4bk964OEy9I9MyxEZj1WEzU",

"sk_euPEY73sIA130ISox0KnU9b1hFR5976Cviqv0BctTI61qNPHO0omv1jao0RkqvM7",
          "sk_6MhuQxtU0IqolwlIJWh75tyPSZSzn7RfjccTYj8mmlL0lHqo0ThKZCQ6k1JQp1E1",
      ]
      threads2 = []
      for api in apis:
        # Create a new Thread object, targeting the send_request function
        thread2 = threading.Thread(target=send_requests_with_threading, args=(api,))
        threads2.append(thread2)
        thread2.start() # Immediately start the thread, running the request concurrently
      for thread2 in threads2:
        thread2.join()
