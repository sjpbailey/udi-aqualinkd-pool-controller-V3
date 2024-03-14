import json
import requests

# GET all devices
response = requests.get('http://192.168.1.100:80/api/devices')
print("Devices")
print(response.text)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print()
# GET Statuses
response1 = requests.get('http://192.168.1.100:80/api/status')
print("Statuses")
print(response1.text)
print(json.dumps(response1.json(), indent=4, sort_keys=True))
print()
# GET Schedules
print("Schedules")
response2 = requests.get('http://192.168.1.100:80/api/status')
print(response2.text)
print(json.dumps(response2.json(), indent=4, sort_keys=True))
print()


print(" Filter Pump")
data = {
    'value': '2895',
}

response3 = requests.put(
    'http://192.168.1.100:80/api/Filter_Pump/RPM/set', data=data)
print(response3.text)
# print(json.dumps(response3.json(), indent=4, sort_keys=True))
print()
