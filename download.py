import requests
import json

headers = {'Content-Type': 'application/json'}
pagesize=2000 #Even though documentation specifies 5000 is the maximum, this is the largest size i can get working

initial_response=requests.get("https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=1",headers=headers)
initial_cves=json.loads(response.content.decode('utf-8'))
total_cves=initial_cves'totalResults']
response=requests.get("https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage={}".format(pagesize),headers=headers)

print (intial_cves['totalResults'])

