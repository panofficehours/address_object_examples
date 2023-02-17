# Python Script to automate address objects

## Methods

- XML API
  - strengths:
    - full API capability
    - XML is extremely powerful
    - XML provides many great tools like XSLT, XPATH
  - weaknesses:
    - XML is kinda complicated
    - XML API has unrestricted to the box
- REST API endpoints
  - strengths:
    - It's JSON!
    - Strong RBAC
  - weaknesses:
    - limited capability
    - laser-focused on managing security configuration
    - PATCH operations are not supported
- pan-os-python SDK
  - strengths:
    - object-oriented configuration of firewall
    - consistent workflow within the SDK
    - supports both PAN-OS and Panorama
  - weaknesses:
    - cannot be used to retrieve state information
    - you must know Python
- Ansible
  - strengths:
    - uses the Python SDK for config changes
    - can also be used to pull state and operational data from device
    - supports Panorama and PAN-OS
    - multithreaded
    - dynamic inventory
    - multi-vendor
  - weaknesses:
    - performance
    - Love for YAML
