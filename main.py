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
	apis = ["a2664670-f890-4379-a189-5f8f96080e95",
	"12da19ac-3d11-483f-b819-818b71e9c570",
	"6a83bc86-2d2d-49e7-800e-32fc668c8575",
	"b088cf6e-770b-4d45-9dba-bf4492edae1f",
	"abc85b80-1b02-4c4f-9863-5bd2033cf9e5",
	"328f761f-8203-4a35-96ac-b15484679bc1",
	"08c5ccd6-dbd5-4968-a8b1-75b66bca9531",
	"ae0b4bb9-eef9-46d4-aee5-787f77f401d7",
	"e25629ef-a2c9-4ab8-8c09-7a07fe6b85d5",
	"7f1ba863-755d-44d6-b745-9408ea65233c",
	"b2cafe42-4df4-4e98-93b9-2397b8e03b03"
	] 
	
	for api in apis:
	    thread = threading.Thread(target=send_request, args=(api,))
	    threads.append(thread)
	    thread.start()
	
	# Wait for all threads to complete
	for thread in threads:
	    thread.join()
	
	print("All requests finished.")
