import requests
import json

headers = {'Content-Type': 'application/json'}
pagesize=2000

response=requests.get("https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage={}".format(pagesize),headers=headers)

intial_cves=json.loads(response.content.decode('utf-8'))

print(response)
print (intial_cves)
