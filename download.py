import requests, json, time


headers = {'Content-Type': 'application/json'}
pagesize=10 #Even though documentation specifies 5000 is the maximum, this is the largest size i can get working
startindex=0
cve_array = []

initial_response=requests.get("https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=0",headers=headers)
initial_cves=json.loads(initial_response.content.decode('utf-8'))
total_cves=initial_cves['totalResults']

## Testing
total_cves=20
#response=requests.get("https://services.nvd.nist.gov/rest/json/cves/1.0?startIndex={}&resultsPerPage={}".format(startindex, pagesize),headers=headers)
#cves=json.loads(response.content.decode('utf-8'))

def dumptofile(json_string):
    with open('output.json','w') as json_file:
        json.dump(json_string, json_file)

while (startindex < total_cves):
    response=requests.get("https://services.nvd.nist.gov/rest/json/cves/1.0?startIndex={}&resultsPerPage={}".format(startindex, pagesize),headers=headers)
    cves=json.loads(response.content.decode('utf-8'))
    for i in cves['result']['CVE_Items']:
        cve_array.append(i)
    time.sleep(5)
    startindex=startindex+pagesize
 
dumptofile(cve_array)
    
