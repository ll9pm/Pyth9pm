# Install the Python Requests library:
# `pip install requests`
import requests
import threading
import time

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
        response = requests.get(
            url='https://api.webscrapingapi.com/v2?',
            params={
                'api_key': api,
                'url': "https://viikqoye.com/dc/?blockID=394155",
                "render_js":"1"
            },
            timeout=30 # Set a timeout to prevent threads from hanging indefinitely
        )
        duration = time.time() - start_time
        print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Finished Request #{request_number}. Status Code: {response.status_code} in {duration:.2f}s")
        # print('Response Body: ', response.content) # Uncomment to see the content
    
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
    for i in range(100):
      
      apis =[
      "4KRIayqxXpltfcanPtZnthqfXIt2n257",
      "fmbyN6PFb0iD36HCLMBmK0DIhCeqEg9c",
       "g5SSb9o4ylvjfttl5L6RTWsHVDNRDdby",
       "zpLHTEBjVrger3TXoxYwub8J4Eo4Eycn",
       "qCAfBWgVc0Uk73QzZH7PXggxp7mW73b7",
       "N2HH5SjPM8159EslYSb4JrlWwVGvR6J4"
  
       
     ]
      threads2 = []
      for api in apis:
        # Create a new Thread object, targeting the send_request function
        thread2 = threading.Thread(target=send_requests_with_threading, args=(api,))
        threads2.append(thread2)
        thread2.start() # Immediately start the thread, running the request concurrently
      for thread2 in threads2:
        thread2.join()
      time.sleep(240)
