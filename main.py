import http.client
import threading

def send_request(api):
    print("start",api)
    url = "/scrape/web"
    payload = "{\"url\":\"https://viikqoye.com/dc/?blockID=394255\",\"proxyType\":\"residential\",\"proxyCountry\":\"US\",\"blockResources\":false,\"blockAds\":false,\"blockUrls\":[],\"wait\":10000,\"jsScenario\":[],\"extractRules\":{\"title\":\"h1\"},\"screenshot\":true,\"jsRendering\":true,\"extractEmails\":false,\"includeOnlyTags\":[],\"excludeTags\":[],\"outputFormat\":[]}"
    headers = {
    'x-api-key': api,
    'Content-Type': "application/json"
}
    try:
        conn = http.client.HTTPSConnection("api.hasdata.com")
        conn.request("POST", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        
        print(f"Request to {url} finished with status: {res.status}")
        # Process the response data as needed
    except Exception as e:
        print(f"Error sending request to {url}: {e}")
    finally:
        conn.close()

# Define your request details

for i in range(110):
	# Create a list of threads
	threads = []
	apis = ["ce584754-f243-4ee4-9bc5-e990ed2662ae",
	"3a021d5e-5858-4395-830f-1ede1821cffb",
	"071b79d0-0d5e-4b4c-898e-3c02200121ac",
	"dc7cc5ec-44fe-4734-a772-dff36add85d3",
	"2aea1ea3-4c50-4cf1-a453-3c28f289fcaf"
	]  # Number of parallel requests
	
	for api in apis:
	    thread = threading.Thread(target=send_request, args=(api,))
	    threads.append(thread)
	    thread.start()
	
	# Wait for all threads to complete
	for thread in threads:
	    thread.join()
	
	print("All requests finished.")
