import requests
import json

url = "https://dallas-vfw-01.redtail.com/restapi/v10.2/Objects/Addresses?location=vsys&vsys=vsys1&name=ghostface"

payload = json.dumps(
    {
        "entry": {
            "@name": "ghostface",
            "ip-netmask": "192.168.88.2/32",
            "tag": {"member": ["Automation"]},
        }
    }
)
headers = {
    "X-PAN-KEY": "LUFRPT1hUnp4R2RZZjRqVUsvRVhqb00rRWxJeHBTZnc9ZHlmUzFaeHhXN2ZBc2ZldExrcWNwVmQ0K0dpRC9OWFBxVm0wVi9nWlFZem04eUxlSXF4dTEwVUFSNFBMSjA1aQ==",
    "Content-Type": "application/json",
    "Cookie": "PHPSESSID=qebqhch47n0hpigqb74uad6ppn",
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
