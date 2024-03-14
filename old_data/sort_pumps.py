import json
import requests


################### Commands ###################################

'''
###### Pump Speed ######
json_data = {"id": 50, "circuits": [
    {"speed": 2200, "units": {"val": 0}, "id": 1, "circuit": 6}]}

response = requests.put(
    'http://192.168.1.53:4200/config/pump', json=json_data)

print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Pump Speed")


###### Pool Start/Stop ######
json_data = {"id": 6, "state": False}  # True-Start False-Stop

response = requests.put(
    'http://192.168.1.53:4200/state/circuit/setState', json=json_data)

print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Start/Stop")

###### Pump Status ######

response = requests.get('https://192.168.1.53:4200/config/options/pumps/')
print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Pump Status?")'''


# headers = {'accept': 'application/json', }
# response = requests.get(
#    'http://192.168.1.53:4200/temps/bodies/setPoint', headers=headers)

# print(response.text)


# x = requests.get('http://192.168.1.53:4200/config/circuits/')
# print(json.dumps(x.json(), indent=4, sort_keys=True))

# "http://192.168.1.53:4200/state/all/"


# "http://192.168.1.53:4200/state/temps/"

y = requests.get("http://192.168.1.53:4200/state/all/")
# print(y.text)
response = (json.dumps(y.json(), indent=4, sort_keys=True))

print(response)


################ CIRCUITS ######################################
"""for i in y:
    print(i[0])  # ["name"], i["id"], i['isOn'])
print()
# ["temps"]["bodies"][0]["setPoint"]))
print("Setpoint {}".format(y["alias"]))
print()"""


# http://192.168.1.53:4200/state/all/systemUnits
# https://192.168.1.53:4201/state/pump/1/
# + [0]["bodies"])
# z = requests.get("http://192.168.1.53:4200/state/pumps/")
# print(json.dumps(z.json(), indent=4, sort_keys=True))
# print(z.text)
# print("Air Temp {}".format(z["circuits"]))
# print()


# print("Pool Running  {}".format(z["temps"]["bodies"][0]["isOn"]))
# q = requests.get('http://192.168.1.53:4200/state/temps/air')
# z = json.dumps(q.json(), indent=4, sort_keys=True)
# print("Setpoint Temp  {}".format(z["temps"]["bodies"][0]["setPoint"]))
# print(z)
# for i in z:
#    print(i)
# print(z.text)


# "http://192.168.1.53:4200/state/circuits/"
# u = requests.get("http://192.168.1.53:4200/state/circuit/6/")
# print(json.dumps(u.json(), indent=4, sort_keys=True))
# print(u.text)


# http://192.168.1.53:4200/config/options/heaters/

# http://192.168.1.53:4200/config/options/schedules/
# temps/bodies/[0]/setPoint
# p = requests.get("http://192.168.1.53:4200/config/options/heaters/")
# print(json.dumps(p.json(), indent=4, sort_keys=True))
# print(p.text)
# "http://192.168.1.53:4200/config/options/schedules/"
# "http://192.168.1.53:4200/config/options/bodies/"
# """

'''headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = 70

response = requests.get(
    'http://192.168.1.53:4200/state/body/setPoint/', headers=headers, json=json_data)
print(response)

print(response)'''

data = {
    "appVersion": "8.0.1",
    "appVersionState": {
        "equipmentType": "appVersion",
        "gitLocalBranch": "master",
        "gitLocalCommit": "a2e1e75549b1246b3757d7deb7f1ddabeb702d92",
        "githubRelease": "8.0.2",
        "installed": "8.0.1",
        "nextCheckTime": "2024-02-27T20:22:55.054-0800",
        "status": {
            "desc": "New version available",
            "name": "behind",
            "val": 1
        }
    },
    "batteryVoltage": 0,
    "chemControllers": [],
    "chemDosers": [],
    "chlorinators": [],
    "circuitGroups": [],
    "circuits": [
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-02-26T03:49:49.559-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 6,
            "isActive": True,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Pool",
            "priority": "manual",
            "showInFeatures": False,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "body": 1,
                "desc": "Pool",
                "hasHeatSource": True,
                "name": "pool",
                "val": 12
            }
        },
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-02-26T00:20:20.334-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 2,
            "isActive": True,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Light",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "desc": "Light",
                "isLight": True,
                "name": "light",
                "val": 4
            }
        },
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-02-25T23:59:07.420-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 3,
            "isActive": True,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Skim",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "desc": "Generic",
                "name": "generic",
                "val": 0
            }
        },
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-02-25T22:24:12.361-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 4,
            "isActive": True,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Sweep",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "desc": "Generic",
                "name": "generic",
                "val": 0
            }
        }
    ],
    "clockMode": {
        "name": "12 Hour",
        "val": 12
    },
    "clockSource": {
        "desc": "Server",
        "name": "server",
        "val": 3
    },
    "controllerType": "nixie",
    "covers": [],
    "delay": {},
    "delays": [],
    "equipment": {
        "bootLoaderVersion": "",
        "controllerType": "nixie",
        "dual": False,
        "equipmentType": "equipment",
        "maxBodies": 1,
        "maxCircuitGroups": 16,
        "maxCircuits": 40,
        "maxFeatures": 32,
        "maxHeaters": 16,
        "maxLightGroups": 16,
        "maxPumps": 16,
        "maxSchedules": 100,
        "maxValves": 32,
        "messages": [],
        "model": "Nixie Single Body",
        "shared": False,
        "single": True,
        "softwareVersion": "1.0.0"
    },
    "features": [],
    "filters": [
        {
            "body": {
                "desc": "Pool",
                "name": "pool",
                "val": 0
            },
            "equipmentType": "filter",
            "filterType": {
                "desc": "Cartridge",
                "hasBackwash": False,
                "name": "cartridge",
                "val": 1
            },
            "id": 1,
            "isOn": False,
            "name": "Filter 1"
        }
    ],
    "freeze": False,
    "heaters": [
        {
            "bodyId": 0,
            "endTime": "2024-02-25T23:22:40.992-0800",
            "equipmentType": "heater",
            "id": 256,
            "isOn": False,
            "name": "Heater 1",
            "shutdownDelay": False,
            "startTime": "2024-02-25T23:20:58.179-0800",
            "startupDelay": False,
            "type": {
                "desc": "Gas Heater",
                "hasAddress": False,
                "name": "gas",
                "val": 1
            }
        }
    ],
    "lightGroups": [],
    "mode": {
        "desc": "Auto",
        "name": "auto",
        "val": 0
    },
    "model": "Nixie Single Body",
    "nextSunrise": "",
    "nextSunset": "",
    "pumps": [
        {
            "address": 96,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-02-26T03:49:49.559-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": False,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "speed": 2200,
                    "units": {
                        "desc": "RPM",
                        "name": "rpm",
                        "val": 0
                    }
                }
            ],
            "command": 4,
            "driveState": 255,
            "equipmentType": "pump",
            "flow": 0,
            "id": 50,
            "isActive": True,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 15,
            "minSpeed": 450,
            "mode": 0,
            "name": "Pump 1",
            "ppc": 0,
            "pumpOnDelay": False,
            "rpm": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "time": 61,
            "type": {
                "desc": "Intelliflo VSF",
                "hasAddress": True,
                "maxCircuits": 8,
                "maxFlow": 130,
                "maxSpeed": 3450,
                "minFlow": 15,
                "minSpeed": 450,
                "name": "vsf",
                "val": 4
            },
            "watts": 0
        }
    ],
    "schedules": [
        {
            "circuit": {
                "action": {
                    "desc": "Ready",
                    "name": "ready",
                    "val": 0
                },
                "endTime": "2024-02-26T03:49:49.559-0800",
                "equipmentType": "circuit",
                "freezeProtect": False,
                "id": 6,
                "isActive": True,
                "isOn": False,
                "manualPriorityActive": False,
                "name": "Pool",
                "priority": "manual",
                "showInFeatures": False,
                "startDelay": False,
                "stopDelay": False,
                "type": {
                    "body": 1,
                    "desc": "Pool",
                    "hasHeatSource": True,
                    "name": "pool",
                    "val": 12
                }
            },
            "clockMode": {
                "name": "12 Hour",
                "val": 12
            },
            "coolSetpoint": 100,
            "display": {
                "desc": "Always",
                "name": "always",
                "val": 0
            },
            "endTime": 710,
            "endTimeType": {
                "desc": "Manual",
                "name": "manual",
                "val": 0
            },
            "equipmentType": "schedule",
            "heatSetpoint": 78,
            "heatSource": {
                "desc": "No Change",
                "name": "nochange",
                "val": 32
            },
            "id": 1,
            "isOn": False,
            "manualPriorityActive": False,
            "scheduleDays": {
                "days": [
                    {
                        "bitval": 64,
                        "desc": "Sunday",
                        "dow": 0,
                        "name": "sun"
                    },
                    {
                        "bitval": 32,
                        "desc": "Saturday",
                        "dow": 6,
                        "name": "sat"
                    },
                    {
                        "bitval": 16,
                        "desc": "Friday",
                        "dow": 5,
                        "name": "fri"
                    },
                    {
                        "bitval": 8,
                        "desc": "Thursday",
                        "dow": 4,
                        "name": "thu"
                    },
                    {
                        "bitval": 4,
                        "desc": "Wednesday",
                        "dow": 3,
                        "name": "wed"
                    },
                    {
                        "bitval": 2,
                        "desc": "Tuesday",
                        "dow": 2,
                        "name": "tue"
                    },
                    {
                        "bitval": 1,
                        "desc": "Monday",
                        "dow": 1,
                        "name": "mon"
                    }
                ],
                "val": 127
            },
            "scheduleTime": {
                "calculated": True,
                "calculatedDate": "2024-02-26T00:00:00.000-0800",
                "endTime": "2024-02-26T11:50:59.999-0800",
                "shouldBeOn": False,
                "startTime": "2024-02-26T10:00:00.000-0800"
            },
            "scheduleType": {
                "days": "multi",
                "desc": "Repeats",
                "endTime": True,
                "heatSetpoint": True,
                "heatSource": True,
                "name": "repeat",
                "startDate": False,
                "startTime": True,
                "val": 128
            },
            "startDate": "2024-02-02T00:00:00.000-0800",
            "startTime": 600,
            "startTimeType": {
                "desc": "Manual",
                "name": "manual",
                "val": 0
            },
            "triggered": False
        }
    ],
    "startTime": "2024-02-25T23:19:23.454-0800",
    "status": {
        "desc": "Ready",
        "name": "ready",
        "percent": 100,
        "val": 1
    },
    "sunrise": "",
    "sunset": "",
    "systemUnits": {
        "desc": "English",
        "name": "english",
        "val": 0
    },
    "temps": {
        "air": 49.15,
        "bodies": [
            {
                "circuit": 6,
                "heatMode": {
                    "desc": "Heater",
                    "name": "heater",
                    "val": 2
                },
                "heatStatus": {
                    "desc": "Off",
                    "name": "off",
                    "val": 0
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
                "isOn": False,
                "name": "Pool",
                "setPoint": 40,
                "showInDashboard": True,
                "startDelay": False,
                "stopDelay": False,
                "temp": 65.91,
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
        "waterSensor1": 62.85,
        "waterSensor2": 63.45
    },
    "time": "2024-02-26T01:00:01.908-0800",
    "valve": 0,
    "valveMode": {},
    "valves": [
        {
            "equipmentType": "valve",
            "id": 50,
            "isActive": True,
            "isDiverted": False,
            "isIntake": False,
            "isReturn": False,
            "name": "Valve Skim",
            "pinId": 0,
            "type": {
                "desc": "Standard",
                "name": "standard",
                "val": 0
            }
        },
        {
            "equipmentType": "valve",
            "id": 51,
            "isActive": True,
            "isDiverted": False,
            "isIntake": False,
            "isReturn": False,
            "name": "Valve Sweep",
            "pinId": 0,
            "type": {
                "desc": "Standard",
                "name": "standard",
                "val": 0
            }
        }
    ],
    "virtualCircuits": [
        {
            "equipmentType": "virtualCircuit",
            "id": 246,
            "isActive": True,
            "isOn": False,
            "name": "Freeze",
            "type": {
                "desc": "Freeze",
                "name": "freeze",
                "val": 246
            }
        },
        {
            "equipmentType": "virtualCircuit",
            "id": 247,
            "isActive": True,
            "isOn": False,
            "name": "Pool/Spa",
            "type": {
                "desc": "Pool/Spa",
                "name": "poolSpa",
                "val": 247
            }
        },
        {
            "equipmentType": "virtualCircuit",
            "id": 244,
            "isActive": True,
            "isOn": False,
            "name": "Pool Heater",
            "type": {
                "desc": "Pool Heater",
                "name": "poolHeater",
                "val": 244
            }
        },
        {
            "equipmentType": "virtualCircuit",
            "id": 258,
            "isActive": True,
            "isOn": False,
            "name": "Any Heater",
            "type": {
                "desc": "Any Heater",
                "name": "anyHeater",
                "val": 258
            }
        }
    ]
}

print()
print("Watts  {}".format(data["pumps"][0]["watts"]))
print()
print("RPM  {}".format(data["pumps"][0]["rpm"]))
print()
print("GPM  {}".format(data["pumps"][0]["flow"]))
print()
print("Status  {}".format(data["pumps"][0]["circuits"][0]["circuit"]["isOn"]))
print()
