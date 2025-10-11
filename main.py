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
	apis = ["6199463b-befe-4207-a3e6-ca747574c2ee",
	"dd39d2b6-b0f0-45f4-afa1-0f7a1c98ecf1",
	"0717ae64-caa0-4e26-94cf-9801e0c92b7a",
	"07db26ca-9b58-4e12-af52-59752b2c5fa3",
	"a0d911ca-8cc7-40ed-813b-5822d65913cb",
	"31e54535-d3dd-43a0-9bcc-32e228c4f978",
	"c1a8c6be-bc01-405d-a356-4aeb9c6d1cbb",
	"e22809cb-1050-4d8a-9dca-7b8d482c752d",
	"887170a8-e390-40a0-a10d-38a69f4f2340",
	"e9db5718-d58d-4bc9-9241-d7e08be1b42c",
	"a2664670-f890-4379-a189-5f8f96080e95"
	] 
	
	for api in apis:
	    thread = threading.Thread(target=send_request, args=(api,))
	    threads.append(thread)
	    thread.start()
	
	# Wait for all threads to complete
	for thread in threads:
	    thread.join()
	
	print("All requests finished.")
