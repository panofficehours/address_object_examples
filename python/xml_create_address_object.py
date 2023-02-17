import requests

url = "https://dallas-vfw-01.redtail.com/api"

payload = "key=LUFRPT1hUnp4R2RZZjRqVUsvRVhqb00rRWxJeHBTZnc9ZHlmUzFaeHhXN2ZBc2ZldExrcWNwVmQ0K0dpRC9OWFBxVm0wVi9nWlFZem04eUxlSXF4dTEwVUFSNFBMSjA1aQ%3D%3D&type=config&action=set&xpath=%2Fconfig%2Fdevices%2Fentry%5B%40name%3D'localhost.localdomain'%5D%2Fvsys%2Fentry%5B%40name%3D'vsys1'%5D%2Faddress-group&element=%3Centry%20name%3D%22Bad%20People%22%3E%3Cstatic%3E%3Cmember%3ETest-Address-Object%3C%2Fmember%3E%3C%2Fstatic%3E%3Cdescription%3Ebad%20actors%3C%2Fdescription%3E%3C%2Fentry%3E"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "X-PAN-KEY": "LUFRPT1hUnp4R2RZZjRqVUsvRVhqb00rRWxJeHBTZnc9ZHlmUzFaeHhXN2ZBc2ZldExrcWNwVmQ0K0dpRC9OWFBxVm0wVi9nWlFZem04eUxlSXF4dTEwVUFSNFBMSjA1aQ==",
    "Cookie": "PHPSESSID=qebqhch47n0hpigqb74uad6ppn",
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
