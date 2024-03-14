import requests
import json


x = requests.get('http://192.168.1.53:4200/config/circuits/')
# print(json.dumps(x.json(), indent=4, sort_keys=True))

# "http://192.168.1.53:4200/config/options/circuits/"
# "http://192.168.1.53:4200/state/all/"
# "http://192.168.1.53:4200/state/temps/"
y = requests.get("http://192.168.1.53:4200/state/temps")
# print(y.text)

# print(y.text)
# print(type(y.text))
response = (json.dumps(y.json(), indent=4, sort_keys=True))

print(response)


z = requests.get("http://192.168.1.53:4200/state/temps/")
# print(json.dumps(z.json(), indent=4, sort_keys=True))
# for temps in z:
#    print(temps[0])
# print(z.text)


a = requests.get("http://192.168.1.53:4200/state/pump/1")
# print(json.dumps(a.json(), indent=4, sort_keys=True))

# "http://192.168.1.53:4200/state/circuits/"
u = requests.get("http://192.168.1.53:4200/state/circuit/6/")
# print(json.dumps(u.json(), indent=4, sort_keys=True))
# print(u.text)


p = requests.get("http://192.168.1.53:4200/config/options/schedules/")
# print(json.dumps(p.json(), indent=4, sort_keys=True))
# print(p.text)
# "http://192.168.1.53:4200/config/options/schedules/"
# "http://192.168.1.53:4200/config/options/bodies/"

"""data = {
    "air": 67.8,
    "bodies": [
        {
            "circuit": 6,
            "heatMode": {
                "desc": "Heater",
                "name": "heater",
                "val": 2
            },
            "heatStatus": {
                "desc": "Heater",
                "name": "heater",
                "val": 1
            },
            "heaterCooldownDelay": False,
            "heaterOptions": {
                "gas": 1,
                "heatpump": 0,
                "hybrid": 0,
                "mastertemp": 0,
                "maxetherm": 0,
                "solar": 0,
                "total": 1,
                "ultratemp": 0
            },
            "id": 1,
            "isCovered": False,
            "isOn": True,
            "name": "Pool",
            "setPoint": 78,
            "showInDashboard": True,
            "startDelay": False,
            "stopDelay": False,
            "temp": 69.89,
            "type": {
                "desc": "Pool",
                "name": "pool",
                "val": 0
            }
        }
    ],
    "equipmentType": "temps",
    "units": {
        "desc": "Fahrenheit",
        "name": "F",
        "val": 0
    },
    "waterSensor1": 68.08,
    "waterSensor2": 0
}


print()
print("Name " + data["bodies"][0]["type"]["name"])
print()
print("Air Temp {}".format(data["air"]))
print()
print("Water Temp {}".format(data["waterSensor1"]))
print()

print("Circuit {}".format(data["bodies"][0]["circuit"]))
print("ID {}".format(data["bodies"][0]["id"]))
print("Heater Name {}".format(data["bodies"][0]["heatMode"]["name"]))
print()
print("Setpoint {}".format(data["bodies"][0]["setPoint"]))
print("Temperature {}".format(data["bodies"][0]["temp"]))
print()

print("Heat Options Gas {}".format(data["bodies"][0]["heaterOptions"]["gas"]))
print()
print("Heat Options HeatPump {}".format(
    data["bodies"][0]["heaterOptions"]["heatpump"]))
print()
print("Heat Options Hybrid {}".format(
    data["bodies"][0]["heaterOptions"]["hybrid"]))
print()
print("Heat Options MasterTemp {}".format(
    data["bodies"][0]["heaterOptions"]["mastertemp"]))
print()
print("Heat Options Maxetherm {}".format(
    data["bodies"][0]["heaterOptions"]["maxetherm"]))
print()
print("Heat Options Solar {}".format(
    data["bodies"][0]["heaterOptions"]["solar"]))
print()
print("Heat Options Ultratemp {}".format(
    data["bodies"][0]["heaterOptions"]["ultratemp"]))
print()
print("Total Heaters {}".format(data["bodies"][0]["heaterOptions"]["total"]))
print()
# print(data["bodies"][0])


# print(data["heater"]["name"])
# print(data["setpoint"])


# Closing file
# f.close()"""
