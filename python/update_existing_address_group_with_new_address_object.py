import requests
import json

# first create the new address object
address_object_url = "https://dallas-vfw-01.redtail.com/restapi/v10.2/Objects/Addresses?location=vsys&vsys=vsys1&name=method-man"

headers = {
    "X-PAN-KEY": "LUFRPT1hUnp4R2RZZjRqVUsvRVhqb00rRWxJeHBTZnc9ZHlmUzFaeHhXN2ZBc2ZldExrcWNwVmQ0K0dpRC9OWFBxVm0wVi9nWlFZem04eUxlSXF4dTEwVUFSNFBMSjA1aQ==",
    "Content-Type": "application/json",
}

new_address_object = {
    "entry": {
        "@name": "method-man",
        "ip-netmask": "192.168.88.3/32",
        "tag": {"member": ["Automation"]},
    }
}


address_object_payload = json.dumps(new_address_object)

response = requests.request(
    "POST",
    address_object_url,
    headers=headers,
    data=address_object_payload,
    verify=False,
)


# retrieve list of existing address group entries
address_group_url = "https://dallas-vfw-01.redtail.com/restapi/v10.2/Objects/AddressGroups?location=vsys&vsys=vsys1&name=Wu-Tang"

address_group_entries = requests.request(
    "GET", address_group_url, headers=headers, verify=False
)

response_dictionary = address_group_entries.json()

existing_entries = response_dictionary["result"]["entry"][0]["static"]["member"]

# update the address group with our new address object
payload = json.dumps(
    {
        "entry": {
            "@name": "Wu-Tang",
            "static": {
                "member": existing_entries + [new_address_object["entry"]["@name"]]
            },
            "tag": {"member": ["Automation"]},
        }
    }
)

response = requests.request(
    "PUT", address_group_url, headers=headers, data=payload, verify=False
)
